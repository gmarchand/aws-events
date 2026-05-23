from __future__ import annotations

import os
import re
from dataclasses import dataclass
from urllib.parse import parse_qs, urlparse

from googleapiclient.discovery import build


@dataclass
class VideoMetadata:
    video_id: str
    title: str
    description: str
    published_at: str
    channel_title: str
    language: str | None
    playlist_id: str | None
    playlist_title: str | None


def parse_youtube_url(url: str) -> dict:
    """Parse a YouTube URL and return dict with video_id and/or playlist_id."""
    url = url.strip()

    # youtu.be short URL
    short = re.match(r"^https?://youtu\.be/([A-Za-z0-9_-]{11})", url)
    if short:
        return {"video_id": short.group(1), "playlist_id": None}

    parsed = urlparse(url)

    if parsed.scheme in ("http", "https"):
        qs = parse_qs(parsed.query)
        video_id = qs.get("v", [None])[0]
        playlist_id = qs.get("list", [None])[0]

        # playlist-only URL
        if playlist_id and not video_id:
            return {"video_id": None, "playlist_id": playlist_id}

        return {"video_id": video_id, "playlist_id": playlist_id}

    # Bare ID: playlist IDs start with PL, UC, etc. (not 11-char video IDs)
    if re.match(r"^[A-Za-z0-9_-]{11}$", url):
        return {"video_id": url, "playlist_id": None}

    # Bare playlist ID
    if re.match(r"^(PL|UC|RD|FL|UU)[A-Za-z0-9_-]+$", url):
        return {"video_id": None, "playlist_id": url}

    return {"video_id": None, "playlist_id": None}


def _youtube_client():
    api_key = os.environ["GOOGLE_API_KEY"]
    return build("youtube", "v3", developerKey=api_key)


def fetch_video_metadata(video_id: str) -> VideoMetadata:
    """Fetch metadata for a single video from YouTube Data API v3."""
    youtube = _youtube_client()
    response = (
        youtube.videos()
        .list(part="snippet", id=video_id)
        .execute()
    )
    item = response.get("items", [])
    if not item:
        raise ValueError(f"Video not found: {video_id}")
    item = item[0]
    snippet = item["snippet"]
    return VideoMetadata(
        video_id=video_id,
        title=snippet["title"],
        description=snippet.get("description", ""),
        published_at=snippet["publishedAt"],
        channel_title=snippet.get("channelTitle", ""),
        language=snippet.get("defaultAudioLanguage"),
        playlist_id=None,
        playlist_title=None,
    )


def fetch_playlist_videos(playlist_id: str) -> list[VideoMetadata]:
    """Fetch all videos in a playlist, paginating through all pages."""
    youtube = _youtube_client()
    video_ids: list[str] = []
    next_page_token = None

    while True:
        kwargs = dict(part="snippet", playlistId=playlist_id, maxResults=50)
        if next_page_token:
            kwargs["pageToken"] = next_page_token

        response = youtube.playlistItems().list(**kwargs).execute()
        for item in response.get("items", []):
            vid = item["snippet"]["resourceId"].get("videoId")
            if vid:
                video_ids.append(vid)

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    if not video_ids:
        return []

    # Fetch playlist title
    pl_response = youtube.playlists().list(part="snippet", id=playlist_id).execute()
    playlist_title = None
    if pl_response.get("items"):
        playlist_title = pl_response["items"][0]["snippet"]["title"]

    # Enrich with Videos.list (batches of 50)
    results: list[VideoMetadata] = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i : i + 50]
        vids_response = (
            youtube.videos()
            .list(part="snippet", id=",".join(batch))
            .execute()
        )
        for item in vids_response.get("items", []):
            snippet = item["snippet"]
            results.append(
                VideoMetadata(
                    video_id=item["id"],
                    title=snippet["title"],
                    description=snippet.get("description", ""),
                    published_at=snippet["publishedAt"],
                    channel_title=snippet.get("channelTitle", ""),
                    language=snippet.get("defaultAudioLanguage"),
                    playlist_id=playlist_id,
                    playlist_title=playlist_title,
                )
            )

    return results
