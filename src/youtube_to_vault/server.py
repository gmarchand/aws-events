from __future__ import annotations

import os
from pathlib import Path

from fastmcp import FastMCP

from youtube_to_vault.core.pipeline import process_playlist, process_video
from youtube_to_vault.core.vault import VaultConfig, VaultWriter
from youtube_to_vault.core.youtube import parse_youtube_url

mcp = FastMCP("youtube-to-vault")


def _resolve_vault_path(vault_path: str | None) -> Path:
    path = vault_path or os.environ.get("VAULT_PATH")
    if not path:
        raise ValueError("vault_path must be provided or VAULT_PATH env var must be set")
    return Path(path)


@mcp.tool()
def add_video(url: str, thematic: str | None = None, vault_path: str | None = None) -> dict:
    """Add a YouTube video to the vault."""
    parsed = parse_youtube_url(url)
    video_id = parsed.get("video_id")
    if not video_id:
        return {"status": "error", "error": f"Could not extract video ID from URL: {url}"}

    config = VaultConfig(vault_path=_resolve_vault_path(vault_path))
    result = process_video(video_id, config, thematic=thematic)
    return {
        "video_id": result.video_id,
        "status": result.status,
        "note_path": str(result.note_path) if result.note_path else None,
        "error": result.error,
    }


@mcp.tool()
def add_playlist(url: str, thematic: str | None = None, vault_path: str | None = None) -> dict:
    """Add all videos from a YouTube playlist to the vault."""
    parsed = parse_youtube_url(url)
    playlist_id = parsed.get("playlist_id")
    if not playlist_id:
        return {"status": "error", "error": f"Could not extract playlist ID from URL: {url}"}

    config = VaultConfig(vault_path=_resolve_vault_path(vault_path))
    results = process_playlist(playlist_id, config, thematic=thematic)

    created = sum(1 for r in results if r.status == "created")
    skipped = sum(1 for r in results if r.status == "skipped")
    errors = sum(1 for r in results if r.status == "error")

    return {
        "total": len(results),
        "created": created,
        "skipped": skipped,
        "errors": errors,
        "results": [
            {
                "video_id": r.video_id,
                "status": r.status,
                "note_path": str(r.note_path) if r.note_path else None,
                "error": r.error,
            }
            for r in results
        ],
    }


@mcp.tool()
def list_thematics(vault_path: str | None = None) -> list[str]:
    """List existing thematic directories in the vault."""
    config = VaultConfig(vault_path=_resolve_vault_path(vault_path))
    writer = VaultWriter(config)
    return writer.get_existing_thematics()


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
