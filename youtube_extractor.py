#!/usr/bin/env python3
"""YouTube Playlist Extractor - Extract videos, transcripts and generate markdown/PDF."""
import os
import re
import subprocess
import time
import requests
import click
import yaml
from pathlib import Path
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
SUPADATA_API_KEY = os.getenv('SUPADATA_API_KEY')

if not GOOGLE_API_KEY:
    raise click.ClickException("GOOGLE_API_KEY not found in .env")


def get_youtube_service():
    return build('youtube', 'v3', developerKey=GOOGLE_API_KEY)


def sanitize_filename(title: str) -> str:
    clean = re.sub(r'[^\w\s-]', '', title)
    return re.sub(r'\s+', '_', clean).strip('_')[:100]


def get_playlist_info(youtube, playlist_id: str) -> tuple[str, str, list]:
    """Get playlist title, channel and videos."""
    pl_resp = youtube.playlists().list(part='snippet', id=playlist_id).execute()
    if not pl_resp['items']:
        raise click.ClickException(f"Playlist {playlist_id} not found")
    
    snippet = pl_resp['items'][0]['snippet']
    playlist_title = snippet['title']
    channel_title = snippet['channelTitle']
    
    videos = []
    next_page = None
    while True:
        items_resp = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page
        ).execute()
        
        for item in items_resp['items']:
            vid_snippet = item['snippet']
            videos.append({
                'id': vid_snippet['resourceId']['videoId'],
                'title': vid_snippet['title'],
                'description': vid_snippet.get('description', ''),
                'published_at': vid_snippet.get('publishedAt', '')[:10]
            })
        
        next_page = items_resp.get('nextPageToken')
        if not next_page:
            break
    
    return playlist_title, channel_title, videos


def get_transcript_supadata(video_id: str) -> list | None:
    """Get transcript using Supadata API."""
    if not SUPADATA_API_KEY:
        return None
    
    url = f"https://api.supadata.ai/v1/youtube/transcript"
    headers = {"x-api-key": SUPADATA_API_KEY}
    params = {"videoId": video_id}
    
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 200:
            data = resp.json()
            content = data.get('content', [])
            return [{'text': c['text'], 'start': c['offset'] / 1000} for c in content]
        elif resp.status_code == 429:
            retry_after = int(resp.headers.get('Retry-After', 10))
            click.echo(f"    Rate limited, waiting {retry_after}s...")
            time.sleep(retry_after)
            return get_transcript_supadata(video_id)
    except Exception as e:
        click.echo(f"    Supadata error: {e}", err=True)
    return None


def format_timestamp(seconds: float) -> str:
    h, r = divmod(int(seconds), 3600)
    m, s = divmod(r, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def create_playlist_markdown(playlist_id: str, playlist_title: str, channel_title: str, videos: list, output_path: Path):
    """Create markdown file listing all videos."""
    with open(output_path, 'w') as f:
        f.write(f"#### [{playlist_title}](https://www.youtube.com/playlist?list={playlist_id}) ")
        f.write(f"created by [{channel_title}](https://www.youtube.com/c/{channel_title.replace(' ', '')})\n\n")
        f.write(f"* video count: {len(videos)} \n\n")
        f.write("| title | Published At |\n")
        f.write("| --- | --- |\n")
        for v in videos:
            f.write(f"| [{v['title']}](https://www.youtube.com/watch?v={v['id']}) | {v['published_at']} |\n")


def create_video_markdown(video: dict, transcript: list | None, output_path: Path) -> bool:
    """Create markdown file for a video."""
    video_id = video['id']
    title = video['title']
    description = video['description']
    base_url = f"https://www.youtube.com/watch?v={video_id}"
    
    with open(output_path, 'w') as f:
        f.write(f"# {title}\n\n")
        f.write(f"[Video Link]({base_url})\n\n")
        
        f.write("## Description\n\n")
        f.write(f"{description or 'No description available.'}\n\n")
        
        f.write("## Transcript\n\n")
        if transcript:
            full_text = ' '.join([e['text'] for e in transcript if e['text']])
            f.write(f"{full_text}\n\n")
        else:
            f.write("No transcript available.\n\n")
        
        f.write("## Subtitles with Timestamps\n\n")
        if transcript:
            for entry in transcript:
                if entry['text']:
                    ts = int(entry['start'])
                    time_str = format_timestamp(ts)
                    link = f"{base_url}&t={ts}s"
                    f.write(f"[{time_str}]({link}) {entry['text']}\n\n")
        else:
            f.write("No subtitles available.\n")
    
    return transcript is not None


def convert_to_pdf(md_path: Path, pdf_path: Path):
    """Convert markdown to PDF using pandoc."""
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    
    cmd = [
        'pandoc', str(md_path), '-o', str(pdf_path),
        '--pdf-engine=xelatex',
        '--toc-depth=3',
        '-V', 'toccolor=black',
        '-V', 'toc-title=Table of Contents',
        '-V', 'documentclass=extarticle',
        '-V', 'geometry:margin=1.2in',
        '-V', 'fontsize=8pt',
        '-V', 'mainfont=DejaVu Sans',
        '-V', 'monofont=DejaVu Sans Mono',
        '-V', 'colorlinks=true',
        '-V', 'linkcolor=blue',
        '-V', 'urlcolor=blue',
        '-V', 'pagestyle=empty',
        '-V', 'linestretch=1.2',
        '-V', 'lang=en-US',
        '-V', 'block-headings',
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise click.ClickException(f"Pandoc failed: {result.stderr[:200]}")


@click.group()
def cli():
    """YouTube Playlist Extractor CLI.
    
    Commands:
      extract          Extract playlists and generate markdown/PDF files
      list-playlists   List all playlists in config
      generate-readme  Generate README.md from playlists config
    """
    pass


@cli.command()
@click.option('--config', '-c', default='playlists.yaml', help='Config file path')
@click.option('--category', '-t', default=None, help='Process only this category')
@click.option('--playlist', '-p', default=None, help='Process only this playlist ID')
@click.option('--skip-pdf', is_flag=True, help='Skip PDF generation')
@click.option('--skip-videos', is_flag=True, help='Skip individual video markdown')
@click.option('--skip-transcript', is_flag=True, help='Skip transcript fetching')
def extract(config, category, playlist, skip_pdf, skip_videos, skip_transcript):
    """Extract playlists and generate markdown/PDF files."""
    config_path = Path(config)
    if not config_path.exists():
        raise click.ClickException(f"Config file not found: {config}")
    
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    
    base_dir = config_path.parent
    output_dir = base_dir / cfg.get('output_dir', 'videos')
    pdf_output_dir = base_dir / cfg.get('pdf_output_dir', 'pdfs')
    
    youtube = get_youtube_service()
    
    if not skip_transcript and not SUPADATA_API_KEY:
        click.echo("Warning: SUPADATA_API_KEY not set, transcripts will be skipped")
        click.echo("Get free API key at https://dash.supadata.ai")
        skip_transcript = True
    
    playlists_cfg = cfg.get('playlists', {})
    
    if category:
        if category not in playlists_cfg:
            raise click.ClickException(f"Category '{category}' not found")
        playlists_cfg = {category: playlists_cfg[category]}
    
    stats = {'videos': 0, 'transcripts': 0, 'pdfs': 0, 'errors': 0}
    
    for cat_name, playlist_ids in playlists_cfg.items():
        click.echo(f"\n{'='*60}")
        click.echo(f"Category: {cat_name}")
        click.echo(f"{'='*60}")
        
        if playlist:
            if playlist not in playlist_ids:
                continue
            playlist_ids = [playlist]
        
        for pl_id in playlist_ids:
            click.echo(f"\nPlaylist: {pl_id}")
            
            try:
                pl_title, channel, videos = get_playlist_info(youtube, pl_id)
                click.echo(f"  Title: {pl_title}")
                click.echo(f"  Videos: {len(videos)}")
                
                cat_dir = output_dir / cat_name
                cat_dir.mkdir(parents=True, exist_ok=True)
                
                pl_md_path = base_dir / f"playlist-{pl_id}.md"
                create_playlist_markdown(pl_id, pl_title, channel, videos, pl_md_path)
                click.echo(f"  Created: {pl_md_path.name}")
                
                if skip_videos:
                    continue
                
                for i, video in enumerate(videos, 1):
                    if video['title'] in ['Private video', 'Deleted video']:
                        click.echo(f"  [{i}/{len(videos)}] Skipping: {video['title']}")
                        continue
                    
                    click.echo(f"  [{i}/{len(videos)}] {video['title'][:50]}...")
                    stats['videos'] += 1
                    
                    transcript = None
                    if not skip_transcript:
                        transcript = get_transcript_supadata(video['id'])
                    
                    filename = sanitize_filename(video['title']) + '.md'
                    video_md_path = cat_dir / filename
                    
                    has_transcript = create_video_markdown(video, transcript, video_md_path)
                    
                    if has_transcript:
                        stats['transcripts'] += 1
                        status = "✓"
                    else:
                        status = "⚠ no transcript"
                    
                    click.echo(f"    {status} -> {filename}")
                    
                    if not skip_pdf:
                        pdf_path = pdf_output_dir / cat_name / filename.replace('.md', '.pdf')
                        try:
                            convert_to_pdf(video_md_path, pdf_path)
                            stats['pdfs'] += 1
                            click.echo(f"    PDF -> {pdf_path.name}")
                        except click.ClickException as e:
                            stats['errors'] += 1
                            click.echo(f"    PDF failed: {e}", err=True)
                
            except Exception as e:
                stats['errors'] += 1
                click.echo(f"  Error: {e}", err=True)
                raise
    
    click.echo(f"\n{'='*60}")
    click.echo(f"Done! Videos: {stats['videos']}, Transcripts: {stats['transcripts']}, PDFs: {stats['pdfs']}, Errors: {stats['errors']}")


@cli.command()
@click.option('--config', '-c', default='playlists.yaml', help='Config file path')
def list_playlists(config):
    """List all playlists in config."""
    config_path = Path(config)
    if not config_path.exists():
        raise click.ClickException(f"Config file not found: {config}")
    
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    
    for cat_name, playlist_ids in cfg.get('playlists', {}).items():
        click.echo(f"\n{cat_name}:")
        for pl_id in playlist_ids:
            click.echo(f"  - {pl_id}")


@cli.command()
@click.option('--config', '-c', default='playlists.yaml', help='Config file path')
@click.option('--output', '-o', default='README.md', help='Output README file')
def generate_readme(config, output):
    """Generate README.md from playlists config."""
    config_path = Path(config)
    if not config_path.exists():
        raise click.ClickException(f"Config file not found: {config}")
    
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    
    youtube = get_youtube_service()
    base_dir = config_path.parent
    output_path = base_dir / output
    
    click.echo(f"Generating {output}...")
    
    with open(output_path, 'w') as f:
        f.write("# AWS Playlists\n\n")
        f.write("This README is automatically generated from `playlists.yaml`.\n\n")
        f.write("To regenerate: `python youtube_extractor.py generate-readme`\n\n")
        
        playlists_cfg = cfg.get('playlists', {})
        
        for cat_name, playlist_ids in playlists_cfg.items():
            # Format category name
            cat_title = cat_name.replace('-', ' ').title()
            f.write(f"## {cat_title}\n\n")
            
            for pl_id in playlist_ids:
                try:
                    # Get playlist info
                    pl_resp = youtube.playlists().list(part='snippet', id=pl_id).execute()
                    if pl_resp['items']:
                        snippet = pl_resp['items'][0]['snippet']
                        pl_title = snippet['title']
                        video_count = youtube.playlists().list(
                            part='contentDetails', 
                            id=pl_id
                        ).execute()['items'][0]['contentDetails']['itemCount']
                        
                        # Write playlist link
                        md_file = f"playlist-{pl_id}.md"
                        f.write(f"- [{pl_title}]({md_file}) ({video_count} videos)\n")
                        click.echo(f"  ✓ {pl_title}")
                    else:
                        f.write(f"- [Playlist {pl_id}](playlist-{pl_id}.md)\n")
                        click.echo(f"  ⚠ Playlist {pl_id} not found")
                except Exception as e:
                    f.write(f"- [Playlist {pl_id}](playlist-{pl_id}.md)\n")
                    click.echo(f"  ✗ Error fetching {pl_id}: {e}")
            
            f.write("\n")
    
    click.echo(f"\n✓ README generated: {output_path}")


if __name__ == '__main__':
    cli()
