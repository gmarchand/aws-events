#!/usr/bin/env python3
import os
import re
import glob
from youtube_transcript_api import YouTubeTranscriptApi
from yt_dlp import YoutubeDL

def sanitize_filename(title):
    clean = re.sub(r'[^\w\s-]', '', title)
    return re.sub(r'\s+', '_', clean).strip('_')

def extract_video_ids_from_playlist(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    channel_match = re.search(r'created by \[([^\]]+)\]', content)
    channel = channel_match.group(1) if channel_match else 'Unknown'
    
    playlist_match = re.search(r'#### \[([^\]]+)\]', content)
    playlist_name = playlist_match.group(1) if playlist_match else 'Unknown'
    
    videos = []
    for match in re.finditer(r'\[([^\]]+)\]\(https://www\.youtube\.com/watch\?v=([^)]+)\)', content):
        title, video_id = match.groups()
        videos.append({'id': video_id, 'title': title})
    
    return channel, playlist_name, videos

def format_timestamp(seconds):
    h, r = divmod(int(seconds), 3600)
    m, s = divmod(r, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"

def get_video_info(video_id):
    opts = {'quiet': True, 'no_warnings': True, 'skip_download': True}
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
        return info.get('title', ''), info.get('description', '')

def get_transcript(video_id):
    try:
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id)
        return [{'text': s.text, 'start': s.start} for s in transcript]
    except Exception:
        try:
            ytt = YouTubeTranscriptApi()
            transcript_list = ytt.list(video_id)
            for t in transcript_list:
                fetched = t.fetch()
                return [{'text': s.text, 'start': s.start} for s in fetched]
        except Exception:
            return None

def create_video_markdown(video_id, title, output_dir):
    print(f"  Processing: {title[:50]}...")
    
    try:
        real_title, description = get_video_info(video_id)
    except Exception as e:
        print(f"    Error getting info: {e}")
        real_title, description = title, ""
    
    transcript = get_transcript(video_id)
    
    filename = sanitize_filename(real_title or title) + '.md'
    filepath = os.path.join(output_dir, filename)
    
    base_url = f"https://www.youtube.com/watch?v={video_id}"
    
    with open(filepath, 'w') as f:
        f.write(f"# {real_title or title}\n\n")
        f.write(f"[Video Link]({base_url})\n\n")
        
        f.write("## Description\n\n")
        f.write(f"{description or 'No description available.'}\n\n")
        
        f.write("## Transcript\n\n")
        if transcript:
            full_text = ' '.join([entry['text'] for entry in transcript])
            f.write(f"{full_text}\n\n")
        else:
            f.write("No transcript available.\n\n")
        
        f.write("## Subtitles with Timestamps\n\n")
        if transcript:
            for entry in transcript:
                ts = int(entry['start'])
                time_str = format_timestamp(ts)
                link = f"{base_url}&t={ts}s"
                f.write(f"[{time_str}]({link}) {entry['text']}\n\n")
        else:
            f.write("No subtitles available.\n")
    
    print(f"    Created: {filename}")
    return filepath

def process_playlist(playlist_file, base_output_dir):
    channel, playlist_name, videos = extract_video_ids_from_playlist(playlist_file)
    
    if not videos:
        print(f"No videos found in {playlist_file}")
        return
    
    dir_name = sanitize_filename(f"{channel}_{playlist_name}")
    output_dir = os.path.join(base_output_dir, dir_name)
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\nProcessing: {playlist_name} ({len(videos)} videos)")
    print(f"Output: {output_dir}")
    
    for video in videos:
        try:
            create_video_markdown(video['id'], video['title'], output_dir)
        except Exception as e:
            print(f"    Error: {e}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, 'videos')
    
    playlist_files = glob.glob(os.path.join(base_dir, 'playlist-*.md'))
    
    print(f"Found {len(playlist_files)} playlist files")
    
    for pf in playlist_files:
        process_playlist(pf, output_dir)

if __name__ == '__main__':
    main()
