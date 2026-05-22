"""Tests for vault.py — AC-6.1 through AC-6.12."""
from __future__ import annotations

from datetime import date

import frontmatter
import pytest

from youtube_to_vault.core.vault import VaultConfig, VaultWriter
from youtube_to_vault.core.youtube import VideoMetadata


@pytest.fixture
def metadata():
    return VideoMetadata(
        video_id="ABC123",
        title="Diffusion du sport en OTT",
        description="Prime Video présente son architecture.",
        published_at="2023-07-27T10:00:00Z",
        channel_title="AWS France",
        language="fr",
        playlist_id="PL123",
        playlist_title="media-symposium",
    )


@pytest.fixture
def writer(tmp_path):
    return VaultWriter(VaultConfig(vault_path=tmp_path))


def test_note_created_at_correct_path(writer, metadata, tmp_path):
    """AC-6.1: Note file created at correct path."""
    path = writer.write_note(metadata, "## Summary\n\nContent.", ["TF1"], ["streaming"], "media")
    assert path.exists()
    assert path.parts[-4] == "media"
    assert path.parts[-3] == "2023"
    assert path.parts[-2] == "media-symposium"
    assert path.suffix == ".md"


def test_frontmatter_has_all_required_fields(writer, metadata):
    """AC-6.2: Frontmatter contains all 12 required fields."""
    path = writer.write_note(metadata, "## Summary\n\nContent.", ["TF1"], ["streaming"], "media")
    post = frontmatter.load(str(path))
    required = {"title", "description", "event", "year", "clients", "tags", "url",
                "video_id", "date", "language", "has_transcript", "thematic", "playlist"}
    assert required.issubset(set(post.keys()))


def test_frontmatter_field_types(writer, metadata):
    """AC-6.3: Frontmatter field types are correct."""
    path = writer.write_note(metadata, "## Summary\n\nContent.", ["TF1"], ["streaming"], "media")
    post = frontmatter.load(str(path))
    assert isinstance(post["year"], int)
    assert isinstance(post["clients"], list)
    assert isinstance(post["has_transcript"], bool)
    assert isinstance(post["date"], date)


def test_client_wikilinks_in_body(writer, metadata):
    """AC-6.4: Client names rendered as wikilinks."""
    path = writer.write_note(metadata, "Summary.", ["TF1", "Canal+"], [], "media")
    body = path.read_text()
    assert "[[TF1]]" in body
    assert "[[Canal+]]" in body


def test_note_exists_after_write(writer, metadata):
    """AC-6.5: note_exists returns True after write."""
    writer.write_note(metadata, "Summary.", [], [], "media")
    assert writer.note_exists("ABC123") is True


def test_note_exists_false_for_unknown(writer):
    """AC-6.6: note_exists returns False for unknown video."""
    assert writer.note_exists("UNKNOWN") is False


def test_note_exists_idempotent(writer, metadata):
    """AC-6.7: note_exists is idempotent."""
    writer.write_note(metadata, "Summary.", [], [], "media")
    assert writer.note_exists("ABC123") == writer.note_exists("ABC123")


def test_update_moc_creates_index(writer, metadata, tmp_path):
    """AC-6.8: update_moc creates _index.md."""
    writer.write_note(metadata, "Summary.", [], [], "media")
    writer.update_moc("media", 2023, "media-symposium")
    index = tmp_path / "media" / "2023" / "media-symposium" / "_index.md"
    assert index.exists()


def test_update_moc_no_duplicates(writer, metadata, tmp_path):
    """AC-6.9: update_moc does not duplicate entries."""
    writer.write_note(metadata, "Summary.", [], [], "media")
    writer.update_moc("media", 2023, "media-symposium")
    writer.update_moc("media", 2023, "media-symposium")
    index = tmp_path / "media" / "2023" / "media-symposium" / "_index.md"
    content = index.read_text()
    slug = "diffusion-du-sport-en-ott"
    assert content.count(slug) == 1


def test_get_existing_thematics_excludes_system_dirs(tmp_path):
    """AC-6.10: get_existing_thematics excludes queries and templates."""
    for d in ["media", "ai", "queries", "templates"]:
        (tmp_path / d).mkdir()
    writer = VaultWriter(VaultConfig(vault_path=tmp_path))
    thematics = writer.get_existing_thematics()
    assert set(thematics) == {"media", "ai"}
    assert "queries" not in thematics
    assert "templates" not in thematics


def test_vault_path_configurable(tmp_path):
    """AC-6.11: Vault path is configurable."""
    custom = tmp_path / "custom_vault"
    custom.mkdir()
    writer = VaultWriter(VaultConfig(vault_path=custom))
    metadata = VideoMetadata(
        video_id="XYZ",
        title="Test Video",
        description="desc",
        published_at="2024-01-01T00:00:00Z",
        channel_title="ch",
        language="en",
        playlist_id=None,
        playlist_title="test-event",
    )
    path = writer.write_note(metadata, "Summary.", [], [], "ai")
    assert str(path).startswith(str(custom))


def test_yaml_special_characters_in_title(writer, tmp_path):
    """AC-6.12: Title with YAML special characters is handled."""
    metadata = VideoMetadata(
        video_id="YAML1",
        title='Video: "AWS" #1',
        description="desc",
        published_at="2024-01-01T00:00:00Z",
        channel_title="ch",
        language="en",
        playlist_id=None,
        playlist_title="test-event",
    )
    path = writer.write_note(metadata, "Summary.", [], [], "media")
    post = frontmatter.load(str(path))
    assert post["title"] == 'Video: "AWS" #1'
