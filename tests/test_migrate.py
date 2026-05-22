"""Tests for scripts/migrate.py — AC-9.1 through AC-9.7."""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import yaml
from click.testing import CliRunner

# Ensure scripts/ is importable
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from migrate import _is_media_category, _is_playlist_id, migrate  # noqa: E402
from youtube_to_vault.core.pipeline import ProcessResult  # noqa: E402


# ---------------------------------------------------------------------------
# AC-9.1 — Media playlists correctly categorized
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("category", ["media-symposium", "ibc", "nab", "media-day", "ibc-2024"])
def test_media_categories_detected(category):
    assert _is_media_category(category) is True


# ---------------------------------------------------------------------------
# AC-9.2 — Non-media playlists correctly categorized
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("category", ["reinvent", "security", "devops", "reinvent-2025", "summit-paris-2024"])
def test_non_media_categories_detected(category):
    assert _is_media_category(category) is False


# ---------------------------------------------------------------------------
# AC-9.3 — Single video ID handled (not playlist)
# ---------------------------------------------------------------------------

def test_single_video_id_detection():
    assert _is_playlist_id("5SfuNwyigN0") is False   # 11-char video ID
    assert _is_playlist_id("PLL_L4MF1Z7JXh5l7") is True
    assert _is_playlist_id("PL2yQDdvlhXf8hzMm") is True


def test_single_video_calls_process_video(tmp_path):
    config = {"playlists": {"media-symposium": ["5SfuNwyigN0"]}}
    config_file = tmp_path / "playlists.yaml"
    config_file.write_text(yaml.dump(config))

    mock_result = ProcessResult(video_id="5SfuNwyigN0", status="created", note_path=tmp_path / "note.md", error=None)

    runner = CliRunner()
    with patch("migrate.process_video", return_value=mock_result) as mock_pv, \
         patch("migrate.process_playlist") as mock_pp:
        result = runner.invoke(migrate, ["--config", str(config_file), "--vault-path", str(tmp_path)])

    assert result.exit_code == 0
    mock_pv.assert_called_once()
    mock_pp.assert_not_called()


# ---------------------------------------------------------------------------
# AC-9.4 — Non-media videos filtered by is_media_client
# ---------------------------------------------------------------------------

def test_non_media_playlist_filters_by_is_media_client(tmp_path):
    config = {"playlists": {"reinvent": ["PL2yQDdvlhXf8hzMm"]}}
    config_file = tmp_path / "playlists.yaml"
    config_file.write_text(yaml.dump(config))

    video1 = MagicMock(video_id="vid1")
    video2 = MagicMock(video_id="vid2")
    video3 = MagicMock(video_id="vid3")

    classification_media = MagicMock(is_media_client=True)
    classification_not_media = MagicMock(is_media_client=False)

    mock_result = ProcessResult(video_id="vid1", status="created", note_path=None, error=None)

    runner = CliRunner()
    with patch("migrate.fetch_playlist_videos", return_value=[video1, video2, video3]), \
         patch("migrate.classify_video", side_effect=[classification_media, classification_not_media, classification_not_media]), \
         patch("migrate.process_video", return_value=mock_result) as mock_pv:
        result = runner.invoke(migrate, ["--config", str(config_file), "--vault-path", str(tmp_path)])

    assert result.exit_code == 0
    # Only video1 (is_media_client=True) should be processed
    assert mock_pv.call_count == 1
    assert mock_pv.call_args[0][0] == "vid1"


# ---------------------------------------------------------------------------
# AC-9.5 — Resume via idempotency (all skipped)
# ---------------------------------------------------------------------------

def test_resume_all_skipped(tmp_path):
    config = {"playlists": {"media-symposium": ["PLL_L4MF1Z7JXh5l7"]}}
    config_file = tmp_path / "playlists.yaml"
    config_file.write_text(yaml.dump(config))

    skipped_result = ProcessResult(video_id="v1", status="skipped", note_path=None, error=None)

    runner = CliRunner()
    with patch("migrate.process_playlist", return_value=[skipped_result, skipped_result]):
        result = runner.invoke(migrate, ["--config", str(config_file), "--vault-path", str(tmp_path)])

    assert result.exit_code == 0
    assert "skipped=2" in result.output


# ---------------------------------------------------------------------------
# AC-9.6 — Progress reported to stdout
# ---------------------------------------------------------------------------

def test_progress_reported(tmp_path):
    config = {"playlists": {"media-symposium": ["PLL_L4MF1Z7JXh5l7"]}}
    config_file = tmp_path / "playlists.yaml"
    config_file.write_text(yaml.dump(config))

    results = [
        ProcessResult(video_id="v1", status="created", note_path=None, error=None),
        ProcessResult(video_id="v2", status="created", note_path=None, error=None),
        ProcessResult(video_id="v3", status="error", note_path=None, error="fail"),
    ]

    runner = CliRunner()
    with patch("migrate.process_playlist", return_value=results):
        result = runner.invoke(migrate, ["--config", str(config_file), "--vault-path", str(tmp_path)])

    assert result.exit_code == 0
    assert "created=2" in result.output
    assert "error=1" in result.output


# ---------------------------------------------------------------------------
# AC-9.7 — CLI accepts required arguments
# ---------------------------------------------------------------------------

def test_cli_accepts_required_args(tmp_path):
    config = {"playlists": {}}
    config_file = tmp_path / "playlists.yaml"
    config_file.write_text(yaml.dump(config))

    runner = CliRunner()
    result = runner.invoke(migrate, ["--config", str(config_file), "--vault-path", str(tmp_path)])

    assert result.exit_code == 0


def test_cli_missing_config_fails(tmp_path):
    runner = CliRunner()
    result = runner.invoke(migrate, ["--config", "/nonexistent.yaml", "--vault-path", str(tmp_path)])
    assert result.exit_code != 0


def test_limit_option(tmp_path):
    """--limit N restricts videos processed per playlist."""
    config = {"playlists": {"media-symposium": ["PLL_L4MF1Z7JXh5l7"]}}
    config_file = tmp_path / "playlists.yaml"
    config_file.write_text(yaml.dump(config))

    results = [
        ProcessResult(video_id=f"v{i}", status="created", note_path=None, error=None)
        for i in range(10)
    ]

    runner = CliRunner()
    with patch("migrate.process_playlist", return_value=results):
        result = runner.invoke(
            migrate,
            ["--config", str(config_file), "--vault-path", str(tmp_path), "--limit", "2"],
        )

    assert result.exit_code == 0
    # With limit=2, only 2 results should be counted
    assert "created=2" in result.output
