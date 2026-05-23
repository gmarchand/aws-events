from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from youtube_to_vault.core.classifier import classify_video, detect_clients, detect_tags
from youtube_to_vault.core.summarizer import generate_summary
from youtube_to_vault.core.transcript import fetch_transcript
from youtube_to_vault.core.vault import VaultConfig, VaultWriter
from youtube_to_vault.core.youtube import VideoMetadata, fetch_playlist_videos, fetch_video_metadata


@dataclass
class ProcessResult:
    video_id: str
    status: str  # "created" | "skipped" | "error"
    note_path: Path | None
    error: str | None


def process_video(
    video_id: str,
    vault_config: VaultConfig,
    thematic: str | None = None,
    event: str | None = None,
    google_api_key: str | None = None,
) -> ProcessResult:
    """Run the full pipeline for a single video."""
    try:
        vault_writer = VaultWriter(vault_config)

        if vault_writer.note_exists(video_id):
            return ProcessResult(video_id=video_id, status="skipped", note_path=None, error=None)

        metadata: VideoMetadata = fetch_video_metadata(video_id)
        # Override playlist_title with event if provided
        if event and not metadata.playlist_title:
            metadata.playlist_title = event

        transcript_result = fetch_transcript(
            video_id,
            preferred_languages=[metadata.language] if metadata.language else None,
        )
        transcript_text = transcript_result.text if transcript_result.available else None

        if thematic is None:
            existing_thematics = vault_writer.get_existing_thematics()
            classification = classify_video(metadata, existing_thematics)
            if classification.thematic is None:
                candidates = classification.candidates
                return ProcessResult(
                    video_id=video_id,
                    status="error",
                    note_path=None,
                    error=f"Low confidence classification. Candidates: {candidates}",
                )
            thematic = classification.thematic

        clients = detect_clients(metadata, transcript_text)
        tags = detect_tags(metadata, transcript_text)
        language = metadata.language or "en"
        summary = generate_summary(transcript_text, metadata.description, metadata, language)

        note_path = vault_writer.write_note(
            metadata=metadata,
            summary=summary,
            clients=clients,
            tags=tags,
            thematic=thematic,
        )
        vault_writer.update_moc(thematic, int(metadata.published_at[:4]), metadata.playlist_title or "unknown")

        return ProcessResult(video_id=video_id, status="created", note_path=note_path, error=None)

    except Exception as exc:  # noqa: BLE001
        return ProcessResult(video_id=video_id, status="error", note_path=None, error=str(exc))


def process_playlist(
    playlist_id: str,
    vault_config: VaultConfig,
    thematic: str | None = None,
    event: str | None = None,
    google_api_key: str | None = None,
) -> list[ProcessResult]:
    """Process all videos in a playlist, isolating failures."""
    videos = fetch_playlist_videos(playlist_id)
    # Use playlist title as event name if not explicitly provided
    playlist_event = event or (videos[0].playlist_title if videos else None)
    results: list[ProcessResult] = []
    for video in videos:
        result = process_video(video.video_id, vault_config, thematic=thematic, event=playlist_event)
        results.append(result)
    return results
