# youtube-to-vault

MCP Server that transforms YouTube videos and playlists into structured Obsidian vault notes with AI-generated summaries.

## Features

- **MCP tools**: `add_video`, `add_playlist`, `list_thematics` — usable from Claude Desktop, Kiro, or any MCP client
- **AI summaries**: Bedrock Claude Opus 4, in the video's language, with structured headings
- **Transcript extraction**: via `youtube-transcript-api` with language priority
- **Thematic classification**: auto-detect or override; media client detection
- **Idempotent**: re-running skips existing notes
- **Migration script**: bootstrap vault from `playlists.yaml`

## Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- AWS credentials with Bedrock access
- Google API key (YouTube Data API v3)

### Install

```bash
uv sync --extra dev
```

### Configure

Copy `.env.example` to `.env` and fill in:

```bash
GOOGLE_API_KEY=your_youtube_api_key
AWS_REGION=us-east-1
VAULT_PATH=/path/to/your/obsidian/vault
```

## Usage

### MCP Server (Claude Desktop / Kiro)

Add to your MCP client config:

```json
{
  "mcpServers": {
    "youtube-to-vault": {
      "command": "uv",
      "args": ["run", "youtube-to-vault"],
      "cwd": "/path/to/aws-events",
      "env": {
        "GOOGLE_API_KEY": "your_key",
        "AWS_REGION": "us-east-1",
        "VAULT_PATH": "/path/to/vault"
      }
    }
  }
}
```

Available tools:
- `add_video(url, thematic?, vault_path?)` — process a single video
- `add_playlist(url, thematic?, vault_path?)` — process all videos in a playlist
- `list_thematics(vault_path?)` — list existing thematic directories

### Migration Script

Bootstrap the vault from `playlists.yaml`:

```bash
uv run python scripts/migrate.py --config playlists.yaml --vault-path vault/

# Limit to 2 videos per playlist (for testing)
uv run python scripts/migrate.py --config playlists.yaml --vault-path vault/ --limit 2
```

## Task Commands

```bash
task setup      # Install dependencies
task lint       # Run ruff linter
task format     # Run ruff formatter
task test       # Run unit tests (excludes integration)
task test-all   # Run all tests
task migrate    # Run migration script
task serve      # Start MCP server
```

## Architecture

```
playlists.yaml
      │
      ▼
scripts/migrate.py ──────────────────────────────────┐
                                                      │
Claude Desktop / Kiro                                 │
      │                                               │
      ▼                                               ▼
src/youtube_to_vault/server.py (FastMCP)    Core Library
      │                                               │
      └──────────────────────────────────────────────┘
                                                      │
                    ┌─────────────────────────────────┤
                    │                                 │
              youtube.py                    classifier.py
           (YouTube API v3)              (Bedrock Claude)
                    │                                 │
              transcript.py               summarizer.py
          (youtube-transcript-api)       (Bedrock Claude)
                    │                                 │
                    └──────────────┬──────────────────┘
                                   │
                               vault.py
                          (Obsidian notes)
                                   │
                                   ▼
                    vault/thematic/year/event/note.md
```

### Vault Structure

```
vault/
├── MOC.md
├── media/
│   └── 2025/
│       └── media-symposium/
│           ├── _index.md
│           └── video-title.md
├── queries/
│   ├── by-client.md
│   ├── by-tag.md
│   └── recent.md
└── templates/
    └── video-note.md
```
