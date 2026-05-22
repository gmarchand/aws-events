"""Tests for server.py — AC-8.1 through AC-8.6."""
from __future__ import annotations

import asyncio
from pathlib import Path
from unittest.mock import patch


from youtube_to_vault.core.pipeline import ProcessResult
from youtube_to_vault.server import mcp

# Valid 11-char YouTube video ID for testing
_VIDEO_ID = "dQw4w9WgXcQ"
_VIDEO_URL = f"https://youtu.be/{_VIDEO_ID}"
_PLAYLIST_ID = "PL123456789"
_PLAYLIST_URL = f"https://youtube.com/playlist?list={_PLAYLIST_ID}"


def run(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


def test_all_three_tools_registered():
    """AC-8.1: All three tools are registered."""
    tools = run(mcp.list_tools())
    tool_names = {t.name for t in tools}
    assert "add_video" in tool_names
    assert "add_playlist" in tool_names
    assert "list_thematics" in tool_names


def test_add_video_parses_url_and_delegates(tmp_path):
    """AC-8.3: add_video parses URL and delegates to pipeline."""
    from youtube_to_vault.server import add_video

    result = ProcessResult(video_id=_VIDEO_ID, status="created", note_path=Path("/tmp/note.md"), error=None)

    with patch("youtube_to_vault.server.process_video", return_value=result) as mock_pv:
        output = add_video(_VIDEO_URL, thematic="media", vault_path=str(tmp_path))

    mock_pv.assert_called_once()
    call_args = mock_pv.call_args
    assert call_args[0][0] == _VIDEO_ID
    assert output["status"] == "created"
    assert output["video_id"] == _VIDEO_ID


def test_add_playlist_parses_url_and_delegates(tmp_path):
    """AC-8.4: add_playlist parses URL and delegates to pipeline."""
    from youtube_to_vault.server import add_playlist

    results = [
        ProcessResult(video_id="V1", status="created", note_path=Path("/tmp/v1.md"), error=None),
        ProcessResult(video_id="V2", status="skipped", note_path=None, error=None),
    ]

    with patch("youtube_to_vault.server.process_playlist", return_value=results) as mock_pp:
        output = add_playlist(_PLAYLIST_URL, thematic="media", vault_path=str(tmp_path))

    mock_pp.assert_called_once()
    call_args = mock_pp.call_args
    assert call_args[0][0] == _PLAYLIST_ID
    assert output["total"] == 2
    assert output["created"] == 1
    assert output["skipped"] == 1
    assert output["errors"] == 0


def test_default_vault_path_from_env(tmp_path, monkeypatch):
    """AC-8.5: Default vault path from VAULT_PATH environment variable."""
    from youtube_to_vault.server import add_video

    monkeypatch.setenv("VAULT_PATH", str(tmp_path))
    result = ProcessResult(video_id=_VIDEO_ID, status="created", note_path=Path("/tmp/note.md"), error=None)

    with patch("youtube_to_vault.server.process_video", return_value=result) as mock_pv:
        add_video(_VIDEO_URL)  # no vault_path param

    mock_pv.assert_called_once()
    call_args = mock_pv.call_args
    vault_config = call_args[0][1]
    assert vault_config.vault_path == tmp_path


def test_list_thematics_returns_vault_directories(tmp_path):
    """AC-8.6: list_thematics returns vault directories."""
    from youtube_to_vault.server import list_thematics

    (tmp_path / "media").mkdir()
    (tmp_path / "ai").mkdir()
    (tmp_path / "queries").mkdir()  # should be excluded

    result = list_thematics(vault_path=str(tmp_path))

    assert "media" in result
    assert "ai" in result
    assert "queries" not in result


def test_add_video_invalid_url(tmp_path):
    """add_video returns error for invalid URL."""
    from youtube_to_vault.server import add_video

    result = add_video("not-a-youtube-url", vault_path=str(tmp_path))
    assert result["status"] == "error"
    assert "video ID" in result["error"]


def test_add_playlist_invalid_url(tmp_path):
    """add_playlist returns error for invalid URL."""
    from youtube_to_vault.server import add_playlist

    result = add_playlist("not-a-playlist-url", vault_path=str(tmp_path))
    assert result["status"] == "error"
    assert "playlist ID" in result["error"]
