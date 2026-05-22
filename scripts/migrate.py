"""Migration script: bootstrap Obsidian vault from playlists.yaml."""
from __future__ import annotations

import os
from pathlib import Path

import click
import yaml
from dotenv import load_dotenv

from youtube_to_vault.core.classifier import classify_video
from youtube_to_vault.core.pipeline import process_playlist, process_video
from youtube_to_vault.core.vault import VaultConfig
from youtube_to_vault.core.youtube import fetch_playlist_videos

load_dotenv()

MEDIA_KEYWORDS = ["media", "symposium", "ibc", "nab", "media-day"]


def _is_media_category(category: str) -> bool:
    cat_lower = category.lower()
    return any(kw in cat_lower for kw in MEDIA_KEYWORDS)


def _is_playlist_id(entry_id: str) -> bool:
    """Return True if entry_id looks like a playlist (starts with PL or PLL_)."""
    return entry_id.startswith("PL") or entry_id.startswith("PLL_")


def _process_entry(
    entry_id: str,
    vault_config: VaultConfig,
    is_media: bool,
    limit: int | None,
) -> dict[str, int]:
    """Process a single playlist or video entry. Returns counts dict."""
    counts = {"created": 0, "skipped": 0, "error": 0}

    if _is_playlist_id(entry_id):
        if is_media:
            results = process_playlist(entry_id, vault_config, thematic="media")
            if limit is not None:
                results = results[:limit]
        else:
            # Fetch videos, classify each, only process media ones
            try:
                videos = fetch_playlist_videos(entry_id)
            except Exception as exc:  # noqa: BLE001
                click.echo(f"  [error] Failed to fetch playlist {entry_id}: {exc}", err=True)
                counts["error"] += 1
                return counts

            if limit is not None:
                videos = videos[:limit]

            results = []
            for video in videos:
                try:
                    classification = classify_video(video, [])
                    if not classification.is_media_client:
                        continue
                except Exception as exc:  # noqa: BLE001
                    click.echo(f"  [error] Classification failed for {video.video_id}: {exc}", err=True)
                    counts["error"] += 1
                    continue
                result = process_video(video.video_id, vault_config, thematic="media")
                results.append(result)
    else:
        # Single video ID
        result = process_video(entry_id, vault_config, thematic="media" if is_media else None)
        results = [result]

    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1

    return counts


@click.command()
@click.option("--config", "config_path", required=True, type=click.Path(exists=True, path_type=Path), help="Path to playlists.yaml")
@click.option("--vault-path", required=True, type=click.Path(path_type=Path), help="Path to Obsidian vault")
@click.option("--limit", default=None, type=int, help="Max videos per playlist (for testing)")
def migrate(config_path: Path, vault_path: Path, limit: int | None) -> None:
    """Migrate playlists.yaml into an Obsidian vault."""
    if not os.environ.get("GOOGLE_API_KEY"):
        click.echo("Warning: GOOGLE_API_KEY not set", err=True)

    with config_path.open() as f:
        config_data = yaml.safe_load(f)

    playlists = config_data.get("playlists", {})
    vault_config = VaultConfig(vault_path=vault_path)

    total = {"created": 0, "skipped": 0, "error": 0}

    for category, entries in playlists.items():
        is_media = _is_media_category(category)
        click.echo(f"\n[{category}] is_media={is_media}, entries={len(entries)}")

        cat_counts = {"created": 0, "skipped": 0, "error": 0}
        for entry_id in entries:
            counts = _process_entry(entry_id, vault_config, is_media, limit)
            for k in cat_counts:
                cat_counts[k] += counts.get(k, 0)

        click.echo(f"  → created={cat_counts['created']} skipped={cat_counts['skipped']} error={cat_counts['error']}")
        for k in total:
            total[k] += cat_counts[k]

    click.echo(f"\nTotal: created={total['created']} skipped={total['skipped']} error={total['error']}")


if __name__ == "__main__":
    migrate()
