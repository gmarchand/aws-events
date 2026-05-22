"""Tests for pipeline.py — AC-7.1 through AC-7.9."""
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from youtube_to_vault.core.classifier import ClassificationResult
from youtube_to_vault.core.pipeline import process_playlist, process_video
from youtube_to_vault.core.transcript import TranscriptResult
from youtube_to_vault.core.vault import VaultConfig
from youtube_to_vault.core.youtube import VideoMetadata


@pytest.fixture
def vault_config(tmp_path):
    return VaultConfig(vault_path=tmp_path)


@pytest.fixture
def metadata():
    return VideoMetadata(
        video_id="ABC123",
        title="AWS Media Day",
        description="A great event.",
        published_at="2023-07-27T10:00:00Z",
        channel_title="AWS France",
        language="fr",
        playlist_id="PL123",
        playlist_title="Media Day 2023",
    )


@pytest.fixture
def transcript_available():
    return TranscriptResult(text="Full transcript text.", language="fr", is_generated=False, available=True)


@pytest.fixture
def transcript_unavailable():
    return TranscriptResult(text="", language="", is_generated=False, available=False)


def _patch_all(
    mock_note_exists=False,
    mock_metadata=None,
    mock_transcript=None,
    mock_classification=None,
    mock_clients=None,
    mock_summary="Summary text.",
    mock_note_path=None,
    mock_thematics=None,
):
    """Return a dict of patches for all pipeline dependencies."""
    return {
        "youtube_to_vault.core.pipeline.VaultWriter.note_exists": MagicMock(return_value=mock_note_exists),
        "youtube_to_vault.core.pipeline.fetch_video_metadata": MagicMock(return_value=mock_metadata),
        "youtube_to_vault.core.pipeline.fetch_transcript": MagicMock(return_value=mock_transcript),
        "youtube_to_vault.core.pipeline.classify_video": MagicMock(return_value=mock_classification),
        "youtube_to_vault.core.pipeline.detect_clients": MagicMock(return_value=mock_clients or []),
        "youtube_to_vault.core.pipeline.generate_summary": MagicMock(return_value=mock_summary),
        "youtube_to_vault.core.pipeline.VaultWriter.write_note": MagicMock(return_value=mock_note_path or Path("/tmp/note.md")),
        "youtube_to_vault.core.pipeline.VaultWriter.update_moc": MagicMock(),
        "youtube_to_vault.core.pipeline.VaultWriter.get_existing_thematics": MagicMock(return_value=mock_thematics or []),
    }


def test_full_pipeline_creates_note(vault_config, metadata, transcript_available):
    """AC-7.1: Full pipeline produces 'created' result."""
    classification = ClassificationResult(thematic="media", confidence=0.95, candidates=[], is_media_client=True)
    patches = _patch_all(
        mock_metadata=metadata,
        mock_transcript=transcript_available,
        mock_classification=classification,
        mock_note_path=Path("/tmp/note.md"),
    )
    with patch.multiple("youtube_to_vault.core.pipeline", **{k.split(".")[-1]: v for k, v in patches.items() if "." not in k.replace("youtube_to_vault.core.pipeline.", "")}):
        with patch("youtube_to_vault.core.pipeline.fetch_video_metadata", return_value=metadata), \
             patch("youtube_to_vault.core.pipeline.fetch_transcript", return_value=transcript_available), \
             patch("youtube_to_vault.core.pipeline.classify_video", return_value=classification), \
             patch("youtube_to_vault.core.pipeline.detect_clients", return_value=[]), \
             patch("youtube_to_vault.core.pipeline.generate_summary", return_value="Summary."), \
             patch.object(__import__("youtube_to_vault.core.vault", fromlist=["VaultWriter"]).VaultWriter, "note_exists", return_value=False), \
             patch.object(__import__("youtube_to_vault.core.vault", fromlist=["VaultWriter"]).VaultWriter, "write_note", return_value=Path("/tmp/note.md")), \
             patch.object(__import__("youtube_to_vault.core.vault", fromlist=["VaultWriter"]).VaultWriter, "update_moc"), \
             patch.object(__import__("youtube_to_vault.core.vault", fromlist=["VaultWriter"]).VaultWriter, "get_existing_thematics", return_value=[]):

            result = process_video("ABC123", vault_config, thematic="media")

    assert result.status == "created"
    assert result.note_path is not None
    assert result.error is None


def test_existing_note_skipped(vault_config, metadata):
    """AC-7.2: Existing note is skipped, no downstream calls."""
    from youtube_to_vault.core.vault import VaultWriter

    with patch.object(VaultWriter, "note_exists", return_value=True), \
         patch("youtube_to_vault.core.pipeline.fetch_video_metadata") as mock_meta, \
         patch("youtube_to_vault.core.pipeline.fetch_transcript") as mock_tr, \
         patch("youtube_to_vault.core.pipeline.classify_video") as mock_cl, \
         patch("youtube_to_vault.core.pipeline.generate_summary") as mock_sm:

        result = process_video("ABC123", vault_config)

    assert result.status == "skipped"
    assert result.note_path is None
    mock_meta.assert_not_called()
    mock_tr.assert_not_called()
    mock_cl.assert_not_called()
    mock_sm.assert_not_called()


def test_thematic_override_skips_classifier(vault_config, metadata, transcript_available):
    """AC-7.3: Thematic override skips classifier."""
    from youtube_to_vault.core.vault import VaultWriter

    with patch.object(VaultWriter, "note_exists", return_value=False), \
         patch.object(VaultWriter, "write_note", return_value=Path("/tmp/note.md")), \
         patch.object(VaultWriter, "update_moc"), \
         patch.object(VaultWriter, "get_existing_thematics", return_value=[]), \
         patch("youtube_to_vault.core.pipeline.fetch_video_metadata", return_value=metadata), \
         patch("youtube_to_vault.core.pipeline.fetch_transcript", return_value=transcript_available), \
         patch("youtube_to_vault.core.pipeline.classify_video") as mock_classify, \
         patch("youtube_to_vault.core.pipeline.detect_clients", return_value=[]), \
         patch("youtube_to_vault.core.pipeline.generate_summary", return_value="Summary."):

        result = process_video("ABC123", vault_config, thematic="media")

    mock_classify.assert_not_called()
    assert result.status == "created"


def test_low_confidence_returns_error_with_candidates(vault_config, metadata, transcript_available):
    """AC-7.4: Low confidence classification returns error with candidates."""
    from youtube_to_vault.core.vault import VaultWriter

    low_conf = ClassificationResult(thematic=None, confidence=0.3, candidates=["media", "ai"], is_media_client=False)

    with patch.object(VaultWriter, "note_exists", return_value=False), \
         patch.object(VaultWriter, "get_existing_thematics", return_value=["media", "ai"]), \
         patch("youtube_to_vault.core.pipeline.fetch_video_metadata", return_value=metadata), \
         patch("youtube_to_vault.core.pipeline.fetch_transcript", return_value=transcript_available), \
         patch("youtube_to_vault.core.pipeline.classify_video", return_value=low_conf):

        result = process_video("ABC123", vault_config)

    assert result.status == "error"
    assert "media" in result.error
    assert "ai" in result.error


def test_transcript_unavailable_passes_none_to_summarizer(vault_config, metadata, transcript_unavailable):
    """AC-7.5: Transcript unavailability falls back to description."""
    from youtube_to_vault.core.vault import VaultWriter

    with patch.object(VaultWriter, "note_exists", return_value=False), \
         patch.object(VaultWriter, "write_note", return_value=Path("/tmp/note.md")), \
         patch.object(VaultWriter, "update_moc"), \
         patch.object(VaultWriter, "get_existing_thematics", return_value=[]), \
         patch("youtube_to_vault.core.pipeline.fetch_video_metadata", return_value=metadata), \
         patch("youtube_to_vault.core.pipeline.fetch_transcript", return_value=transcript_unavailable), \
         patch("youtube_to_vault.core.pipeline.detect_clients", return_value=[]), \
         patch("youtube_to_vault.core.pipeline.generate_summary", return_value="Summary.") as mock_summary:

        result = process_video("ABC123", vault_config, thematic="media")

    # generate_summary called with transcript=None
    call_args = mock_summary.call_args
    assert call_args[0][0] is None or call_args[1].get("transcript") is None
    assert result.status == "created"


def test_one_video_failure_does_not_block_others(vault_config, metadata):
    """AC-7.6: One video failure does not block others in playlist."""
    from youtube_to_vault.core.vault import VaultWriter

    videos = [
        VideoMetadata("V1", "Title 1", "Desc", "2023-01-01T00:00:00Z", "Ch", "fr", "PL1", "Playlist"),
        VideoMetadata("V2", "Title 2", "Desc", "2023-01-01T00:00:00Z", "Ch", "fr", "PL1", "Playlist"),
        VideoMetadata("V3", "Title 3", "Desc", "2023-01-01T00:00:00Z", "Ch", "fr", "PL1", "Playlist"),
    ]

    call_count = [0]

    def fake_fetch_metadata(video_id):
        call_count[0] += 1
        if video_id == "V2":
            raise RuntimeError("API error for V2")
        return next(v for v in videos if v.video_id == video_id)

    transcript = TranscriptResult(text="text", language="fr", is_generated=False, available=True)

    with patch("youtube_to_vault.core.pipeline.fetch_playlist_videos", return_value=videos), \
         patch.object(VaultWriter, "note_exists", return_value=False), \
         patch.object(VaultWriter, "write_note", return_value=Path("/tmp/note.md")), \
         patch.object(VaultWriter, "update_moc"), \
         patch.object(VaultWriter, "get_existing_thematics", return_value=[]), \
         patch("youtube_to_vault.core.pipeline.fetch_video_metadata", side_effect=fake_fetch_metadata), \
         patch("youtube_to_vault.core.pipeline.fetch_transcript", return_value=transcript), \
         patch("youtube_to_vault.core.pipeline.detect_clients", return_value=[]), \
         patch("youtube_to_vault.core.pipeline.generate_summary", return_value="Summary."):

        results = process_playlist("PL1", vault_config, thematic="media")

    assert len(results) == 3
    statuses = {r.video_id: r.status for r in results}
    assert statuses["V1"] == "created"
    assert statuses["V2"] == "error"
    assert statuses["V3"] == "created"


def test_existing_thematics_passed_to_classifier(vault_config, metadata, transcript_available):
    """AC-7.7: existing_thematics passed to classifier."""
    from youtube_to_vault.core.vault import VaultWriter

    classification = ClassificationResult(thematic="media", confidence=0.9, candidates=[], is_media_client=True)

    with patch.object(VaultWriter, "note_exists", return_value=False), \
         patch.object(VaultWriter, "write_note", return_value=Path("/tmp/note.md")), \
         patch.object(VaultWriter, "update_moc"), \
         patch.object(VaultWriter, "get_existing_thematics", return_value=["media", "ai"]), \
         patch("youtube_to_vault.core.pipeline.fetch_video_metadata", return_value=metadata), \
         patch("youtube_to_vault.core.pipeline.fetch_transcript", return_value=transcript_available), \
         patch("youtube_to_vault.core.pipeline.classify_video", return_value=classification) as mock_classify, \
         patch("youtube_to_vault.core.pipeline.detect_clients", return_value=[]), \
         patch("youtube_to_vault.core.pipeline.generate_summary", return_value="Summary."):

        process_video("ABC123", vault_config)  # no thematic — triggers classification

    mock_classify.assert_called_once()
    _, kwargs = mock_classify.call_args
    existing = kwargs.get("existing_thematics") or mock_classify.call_args[0][1]
    assert "media" in existing
    assert "ai" in existing


def test_result_count_equals_video_count(vault_config):
    """AC-7.8: Result count equals input video count."""
    from youtube_to_vault.core.vault import VaultWriter

    videos = [
        VideoMetadata(f"V{i}", f"Title {i}", "Desc", "2023-01-01T00:00:00Z", "Ch", "fr", "PL1", "Playlist")
        for i in range(5)
    ]
    transcript = TranscriptResult(text="text", language="fr", is_generated=False, available=True)

    with patch("youtube_to_vault.core.pipeline.fetch_playlist_videos", return_value=videos), \
         patch.object(VaultWriter, "note_exists", return_value=False), \
         patch.object(VaultWriter, "write_note", return_value=Path("/tmp/note.md")), \
         patch.object(VaultWriter, "update_moc"), \
         patch.object(VaultWriter, "get_existing_thematics", return_value=[]), \
         patch("youtube_to_vault.core.pipeline.fetch_video_metadata", side_effect=lambda vid: next(v for v in videos if v.video_id == vid)), \
         patch("youtube_to_vault.core.pipeline.fetch_transcript", return_value=transcript), \
         patch("youtube_to_vault.core.pipeline.detect_clients", return_value=[]), \
         patch("youtube_to_vault.core.pipeline.generate_summary", return_value="Summary."):

        results = process_playlist("PL1", vault_config, thematic="media")

    assert len(results) == len(videos)


def test_all_result_statuses_valid(vault_config):
    """AC-7.9: All result statuses are valid values."""
    from youtube_to_vault.core.vault import VaultWriter

    videos = [
        VideoMetadata("V1", "Title 1", "Desc", "2023-01-01T00:00:00Z", "Ch", "fr", "PL1", "Playlist"),
        VideoMetadata("V2", "Title 2", "Desc", "2023-01-01T00:00:00Z", "Ch", "fr", "PL1", "Playlist"),
    ]
    transcript = TranscriptResult(text="text", language="fr", is_generated=False, available=True)

    def fake_meta(vid):
        if vid == "V2":
            raise RuntimeError("fail")
        return next(v for v in videos if v.video_id == vid)

    with patch("youtube_to_vault.core.pipeline.fetch_playlist_videos", return_value=videos), \
         patch.object(VaultWriter, "note_exists", return_value=False), \
         patch.object(VaultWriter, "write_note", return_value=Path("/tmp/note.md")), \
         patch.object(VaultWriter, "update_moc"), \
         patch.object(VaultWriter, "get_existing_thematics", return_value=[]), \
         patch("youtube_to_vault.core.pipeline.fetch_video_metadata", side_effect=fake_meta), \
         patch("youtube_to_vault.core.pipeline.fetch_transcript", return_value=transcript), \
         patch("youtube_to_vault.core.pipeline.detect_clients", return_value=[]), \
         patch("youtube_to_vault.core.pipeline.generate_summary", return_value="Summary."):

        results = process_playlist("PL1", vault_config, thematic="media")

    valid_statuses = {"created", "skipped", "error"}
    for r in results:
        assert r.status in valid_statuses
