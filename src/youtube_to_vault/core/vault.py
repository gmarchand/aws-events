from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import frontmatter

from youtube_to_vault.core.youtube import VideoMetadata


@dataclass
class VaultConfig:
    vault_path: Path


_EXCLUDED_DIRS = {"queries", "templates"}


def _slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")[:80]


class VaultWriter:
    def __init__(self, config: VaultConfig) -> None:
        self._vault = config.vault_path

    def note_exists(self, video_id: str) -> bool:
        """Return True if any note in the vault has this video_id in its frontmatter."""
        for md_file in self._vault.rglob("*.md"):
            try:
                post = frontmatter.load(str(md_file))
                if post.get("video_id") == video_id:
                    return True
            except Exception:  # noqa: BLE001
                continue
        return False

    def write_note(
        self,
        metadata: VideoMetadata,
        summary: str,
        clients: list[str],
        tags: list[str],
        thematic: str,
    ) -> Path:
        """Write an Obsidian note and return its path."""
        published = metadata.published_at[:10]  # YYYY-MM-DD
        year = int(published[:4])
        event = metadata.playlist_title or "unknown"
        event_slug = _slugify(event)
        slug = _slugify(metadata.title)

        note_dir = self._vault / thematic / str(year) / event_slug
        note_dir.mkdir(parents=True, exist_ok=True)
        note_path = note_dir / f"{slug}.md"

        url = f"https://www.youtube.com/watch?v={metadata.video_id}"
        wikilinks = " ".join(f"[[{c}]]" for c in clients) if clients else ""

        fm = {
            "title": metadata.title,
            "description": metadata.description[:500],
            "event": event_slug,
            "year": year,
            "clients": clients,
            "tags": tags,
            "url": url,
            "video_id": metadata.video_id,
            "date": date.fromisoformat(published),
            "language": metadata.language or "en",
            "has_transcript": bool(summary and len(summary) > 50),
            "thematic": thematic,
            "playlist": metadata.playlist_title or "",
        }

        body = (
            f"# {metadata.title}\n\n"
            f"> [!info] Video\n"
            f"> 📺 [Watch on YouTube]({url})\n"
            f"> 📅 {published} | 🎤 {event_slug} | 🌐 {fm['language']}\n"
        )
        if wikilinks:
            body += f"> 🏢 Clients: {wikilinks}\n"
        body += f"\n{summary}\n"

        post = frontmatter.Post(body, **fm)
        note_path.write_text(frontmatter.dumps(post), encoding="utf-8")
        return note_path

    def update_moc(self, thematic: str, year: int, event: str) -> None:
        """Create or update _index.md in the event directory with links to all notes."""
        event_slug = _slugify(event)
        event_dir = self._vault / thematic / str(year) / event_slug
        event_dir.mkdir(parents=True, exist_ok=True)
        index_path = event_dir / "_index.md"

        # Collect existing note links (exclude _index.md itself)
        links: list[str] = []
        for md_file in sorted(event_dir.glob("*.md")):
            if md_file.name == "_index.md":
                continue
            try:
                post = frontmatter.load(str(md_file))
                title = post.get("title", md_file.stem)
            except Exception:  # noqa: BLE001
                title = md_file.stem
            link = f"- [[{md_file.stem}|{title}]]"
            links.append(link)

        content = f"# {event}\n\n" + "\n".join(links) + "\n"
        index_path.write_text(content, encoding="utf-8")

    def get_existing_thematics(self) -> list[str]:
        """List top-level vault directories, excluding system dirs."""
        if not self._vault.exists():
            return []
        return [
            d.name
            for d in self._vault.iterdir()
            if d.is_dir() and d.name not in _EXCLUDED_DIRS
        ]
