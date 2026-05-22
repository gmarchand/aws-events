"""Tests for youtube.py — AC-2.1 through AC-2.6."""
import pytest
from unittest.mock import MagicMock

from youtube_to_vault.core.youtube import (
    fetch_playlist_videos,
    fetch_video_metadata,
    parse_youtube_url,
)


# ---------------------------------------------------------------------------
# AC-2.1 — URL parsing covers all YouTube URL formats
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("url,expected_video_id", [
    ("https://youtu.be/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
    ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "dQw4w9WgXcQ"),
    ("https://youtube.com/watch?v=dQw4w9WgXcQ", "dQw4w9WgXcQ"),
    ("https://youtube.com/watch?v=dQw4w9WgXcQ&list=PL123", "dQw4w9WgXcQ"),
    ("dQw4w9WgXcQ", "dQw4w9WgXcQ"),  # bare video ID
])
def test_parse_youtube_url_video_id(url, expected_video_id):
    result = parse_youtube_url(url)
    assert result["video_id"] == expected_video_id


def test_parse_youtube_url_idempotent():
    """PBT property: parse(parse(url)).video_id == parse(url).video_id"""
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    first = parse_youtube_url(url)
    # Re-parse the video_id as a bare string
    second = parse_youtube_url(first["video_id"])
    assert second["video_id"] == first["video_id"]


# ---------------------------------------------------------------------------
# AC-2.2 — Playlist URL parsing
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("url,expected_playlist_id", [
    ("https://youtube.com/playlist?list=PL123", "PL123"),
    ("PL123", "PL123"),
])
def test_parse_youtube_url_playlist(url, expected_playlist_id):
    result = parse_youtube_url(url)
    assert result["playlist_id"] == expected_playlist_id
    assert result["video_id"] is None


# ---------------------------------------------------------------------------
# AC-2.3 — Video metadata fields populated
# ---------------------------------------------------------------------------

def _mock_youtube_client(mocker, videos_response):
    mock_client = MagicMock()
    mock_client.videos.return_value.list.return_value.execute.return_value = videos_response
    mocker.patch("youtube_to_vault.core.youtube._youtube_client", return_value=mock_client)
    return mock_client


def test_fetch_video_metadata_all_fields(mocker):
    videos_response = {
        "items": [{
            "id": "TRma3Bw1hUI",
            "snippet": {
                "title": "Test Video",
                "description": "A test description",
                "publishedAt": "2023-07-27T10:00:00Z",
                "channelTitle": "AWS France",
                "defaultAudioLanguage": "fr",
            }
        }]
    }
    _mock_youtube_client(mocker, videos_response)

    result = fetch_video_metadata("TRma3Bw1hUI")

    assert result.video_id == "TRma3Bw1hUI"
    assert result.title == "Test Video"
    assert result.description == "A test description"
    assert result.published_at == "2023-07-27T10:00:00Z"
    assert result.channel_title == "AWS France"
    assert result.language == "fr"


# ---------------------------------------------------------------------------
# AC-2.4 — Missing defaultAudioLanguage yields language=None
# ---------------------------------------------------------------------------

def test_fetch_video_metadata_no_language(mocker):
    videos_response = {
        "items": [{
            "id": "ABC123",
            "snippet": {
                "title": "No Language Video",
                "description": "",
                "publishedAt": "2023-01-01T00:00:00Z",
                "channelTitle": "Channel",
                # no defaultAudioLanguage
            }
        }]
    }
    _mock_youtube_client(mocker, videos_response)

    result = fetch_video_metadata("ABC123")
    assert result.language is None


# ---------------------------------------------------------------------------
# AC-2.5 — Playlist pagination collects all videos
# ---------------------------------------------------------------------------

def test_fetch_playlist_videos_pagination(mocker):
    page1 = {
        "items": [{"snippet": {"resourceId": {"videoId": "VID001"}}}],
        "nextPageToken": "TOKEN1",
    }
    page2 = {
        "items": [{"snippet": {"resourceId": {"videoId": "VID002"}}}],
        # no nextPageToken
    }
    playlist_response = {
        "items": [{"snippet": {"title": "Test Playlist"}}]
    }
    videos_batch = {
        "items": [
            {
                "id": "VID001",
                "snippet": {
                    "title": "Video 1", "description": "", "publishedAt": "2023-01-01T00:00:00Z",
                    "channelTitle": "Ch",
                }
            },
            {
                "id": "VID002",
                "snippet": {
                    "title": "Video 2", "description": "", "publishedAt": "2023-01-02T00:00:00Z",
                    "channelTitle": "Ch",
                }
            },
        ]
    }

    mock_client = MagicMock()
    # playlistItems().list() called twice (page1, page2)
    mock_client.playlistItems.return_value.list.return_value.execute.side_effect = [page1, page2]
    mock_client.playlists.return_value.list.return_value.execute.return_value = playlist_response
    mock_client.videos.return_value.list.return_value.execute.return_value = videos_batch
    mocker.patch("youtube_to_vault.core.youtube._youtube_client", return_value=mock_client)

    results = fetch_playlist_videos("PL_TEST")

    assert len(results) == 2
    video_ids = {r.video_id for r in results}
    assert video_ids == {"VID001", "VID002"}
    assert all(r.playlist_id == "PL_TEST" for r in results)
    assert all(r.playlist_title == "Test Playlist" for r in results)


# ---------------------------------------------------------------------------
# AC-2.6 — Empty playlist returns empty list
# ---------------------------------------------------------------------------

def test_fetch_playlist_videos_empty(mocker):
    empty_response = {"items": []}
    mock_client = MagicMock()
    mock_client.playlistItems.return_value.list.return_value.execute.return_value = empty_response
    mocker.patch("youtube_to_vault.core.youtube._youtube_client", return_value=mock_client)

    results = fetch_playlist_videos("PL_EMPTY")
    assert results == []
