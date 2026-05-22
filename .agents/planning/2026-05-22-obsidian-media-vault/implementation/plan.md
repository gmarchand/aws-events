# Implementation Plan

## Checklist

- [ ] Step 1: Project scaffolding and repo cleanup
- [ ] Step 2: Core library — YouTube fetcher
- [ ] Step 3: Core library — Transcript extractor
- [ ] Step 4: Core library — LLM Classifier
- [ ] Step 5: Core library — AI Summarizer
- [ ] Step 6: Core library — Vault Writer
- [ ] Step 7: Core library — Pipeline orchestrator
- [ ] Step 8: MCP Server
- [ ] Step 9: Migration script
- [ ] Step 10: Taskfile and documentation

## Step 1: Project scaffolding and repo cleanup

**Objective**: Set up the new project structure with uv, move legacy files, delete obsolete ones.

**Implementation guidance**:
- Initialize uv project with `pyproject.toml`
- Create package structure: `src/youtube_to_vault/{core/,server.py}`, `scripts/`, `tests/`
- Move `playlist-*.md` files to `playlists/` directory
- Move `extract_videos.py`, `find_reinvent_playlists.py`, `feedly_to_markdown.py`, `youtube-playlist-markdown.py` to `scripts/legacy/`
- Delete `package.json`, `node_modules` (if any), `my-playlist-reinvent-*.md`
- Keep `playlists.yaml` at root, keep `decks/`
- Add dependencies: `fastmcp`, `youtube-transcript-api`, `google-api-python-client`, `boto3`, `python-frontmatter`, `pyyaml`, `tenacity` (retry), `click` (migration CLI)
- Create `.env.example` with `GOOGLE_API_KEY`, `AWS_REGION`

**Test requirements**: `uv sync` succeeds, `python -c "import youtube_to_vault"` works.

**Integration**: Foundation for all subsequent steps.

**Demo**: Clean repo structure, importable package, all dependencies resolved.

## Step 2: Core library — YouTube fetcher

**Objective**: Implement `youtube.py` — fetch video metadata and playlist contents from YouTube Data API v3.

**Implementation guidance**:
- `VideoMetadata` dataclass with all fields
- `fetch_video_metadata(video_id)` — calls Videos.list API
- `fetch_playlist_videos(playlist_id)` — paginates PlaylistItems.list, enriches with Videos.list for descriptions
- Handle single video IDs (not playlists) from `playlists.yaml`
- Extract `defaultAudioLanguage` when available
- Parse YouTube URLs to extract video/playlist IDs

**Test requirements**:
- Unit test with mocked YouTube API responses
- Test URL parsing (various YouTube URL formats)
- Test pagination handling

**Integration**: Used by pipeline.py and migration script.

**Demo**: `fetch_playlist_videos("PLL_L4MF1Z7JWsJi_LUyEMpLaUirkIz2Do")` returns list of VideoMetadata.

## Step 3: Core library — Transcript extractor

**Objective**: Implement `transcript.py` — fetch transcripts with language priority and error handling.

**Implementation guidance**:
- `fetch_transcript(video_id, preferred_languages)` returns `TranscriptResult`
- Language priority: video's language first, then `['fr', 'en']` fallback
- Handle all exception types: `TranscriptsDisabled`, `NoTranscriptFound`, `IpBlocked`, etc.
- Return `TranscriptResult(available=False)` on failure (don't raise)
- Concatenate transcript segments into full text
- Use `tenacity` for retry with exponential backoff on `IpBlocked`/`RequestBlocked`

**Test requirements**:
- Unit test with mocked youtube-transcript-api
- Test language fallback logic
- Test error handling for each exception type
- Test retry behavior

**Integration**: Called by pipeline after metadata fetch.

**Demo**: `fetch_transcript("TRma3Bw1hUI", ["fr", "en"])` returns TranscriptResult with full text.

## Step 4: Core library — LLM Classifier

**Objective**: Implement `classifier.py` — classify videos by thematic and detect media clients via Bedrock.

**Implementation guidance**:
- `classify_video(metadata, existing_thematics)` — sends title+description to Bedrock, asks to classify into existing thematics or suggest new one
- `detect_clients(metadata, transcript)` — extracts client/company names from content
- Use Bedrock Converse API with Claude Opus 4
- System prompt instructs structured JSON output: `{"thematic": "...", "confidence": 0.9, "candidates": [...], "is_media_client": true}`
- Retry with `tenacity` on ThrottlingException
- Minimal token usage: only title+description for classification (not full transcript)

**Test requirements**:
- Unit test with mocked Bedrock responses
- Test JSON parsing of LLM output
- Test fallback when LLM returns unexpected format
- Test confidence threshold logic

**Integration**: Called by pipeline before summarization.

**Demo**: `classify_video(metadata, ["media", "ai"])` returns ClassificationResult.

## Step 5: Core library — AI Summarizer

**Objective**: Implement `summarizer.py` — generate structured summaries via Bedrock Claude Opus 4.

**Implementation guidance**:
- `generate_summary(transcript, description, metadata, language)` → markdown string
- System prompt encodes all summarization rules (active voice, 3 heading levels, formal tone, no bullets, narrative prose)
- If transcript available: summarize transcript
- If no transcript: summarize from description (shorter output expected)
- Include instruction to write in the video's language
- Use Converse API with `maxTokens=4096`, `temperature=0.3`
- Retry with tenacity on throttling

**Test requirements**:
- Unit test with mocked Bedrock response
- Test with transcript input vs description-only input
- Test language instruction is included in prompt

**Integration**: Called by pipeline after transcript extraction.

**Demo**: `generate_summary(transcript_text, description, metadata, "fr")` returns formatted markdown summary.

## Step 6: Core library — Vault Writer

**Objective**: Implement `vault.py` — write Obsidian notes with frontmatter, manage vault structure, generate MOCs.

**Implementation guidance**:
- `VaultWriter` class with configurable vault path
- `note_exists(video_id)` — scan frontmatter of existing notes for matching video_id (or check by filename pattern)
- `write_note(...)` — generates frontmatter YAML + note body with callout + summary, writes to `thematic/year/playlist/slug.md`
- `update_moc(thematic, year, playlist_title)` — updates/creates `_index.md` with links to notes in that directory
- `get_existing_thematics()` — lists top-level directories in vault (excluding queries/, templates/)
- Use `python-frontmatter` for frontmatter handling
- Slugify video titles for filenames
- Insert wikilinks `[[ClientName]]` in note body

**Test requirements**:
- Unit test: write_note creates correct file with valid frontmatter
- Unit test: note_exists detects duplicates
- Unit test: update_moc generates valid markdown with links
- Unit test: get_existing_thematics returns directory names
- Test with temp directory

**Integration**: Final step in pipeline, called after summarization.

**Demo**: `writer.write_note(...)` creates `vault/media/2023/media-symposium/diffusion-sport-ott.md` with full frontmatter and summary.

## Step 7: Core library — Pipeline orchestrator

**Objective**: Implement `pipeline.py` — orchestrate the full video processing flow.

**Implementation guidance**:
- `process_video(video_id, vault_config, thematic)` — full pipeline: fetch → transcript → classify → summarize → write
- `process_playlist(playlist_id, vault_config, thematic)` — iterate videos, process each, collect results
- Idempotency: check `note_exists` before processing
- Error isolation: catch exceptions per video, return ProcessResult with status
- Pass `existing_thematics` to classifier from vault writer
- If thematic provided, skip classification
- If classification fails (low confidence, no thematic param), return error with candidates

**Test requirements**:
- Unit test: full pipeline with all dependencies mocked
- Test idempotency (skip existing)
- Test error isolation (one video fails, others continue)
- Test thematic override vs auto-detection

**Integration**: Used by MCP Server tools and migration script.

**Demo**: `process_playlist("PLL_L4MF1Z7JWsJi_LUyEMpLaUirkIz2Do", config, "media")` processes all videos, returns results.

## Step 8: MCP Server

**Objective**: Implement FastMCP server with `add_video`, `add_playlist`, `list_thematics` tools.

**Implementation guidance**:
- Use FastMCP decorator pattern: `@mcp.tool()`
- `add_video(url, thematic=None, vault_path=None)` — parse URL, call `process_video`
- `add_playlist(url, thematic=None, vault_path=None)` — parse URL, call `process_playlist`
- `list_thematics(vault_path=None)` — call `vault.get_existing_thematics()`
- Default vault_path from environment variable or server config
- Return structured results (JSON-friendly)
- Server entry point: `python -m youtube_to_vault.server`

**Test requirements**:
- Test tool registration (tools are discoverable)
- Test URL parsing in tool handlers
- Test default vault_path resolution
- Integration test: invoke tool via FastMCP test client

**Integration**: This IS the MCP server — the product.

**Demo**: MCP client calls `add_video` with a YouTube URL, note appears in vault.

## Step 9: Migration script

**Objective**: Implement `scripts/migrate.py` — bootstrap vault from existing playlists.yaml.

**Implementation guidance**:
- Read `playlists.yaml`, identify media playlists by category name (media-symposium, ibc, nab, media-day keywords)
- For media playlists: call `process_playlist(id, config, thematic="media")` for each
- For other playlists: fetch video list, classify each by title, process only those with `is_media_client=True`
- CLI with click: `python scripts/migrate.py --config playlists.yaml --vault-path vault/`
- Progress reporting (video count, success/skip/error)
- Resume capability via idempotency (re-run skips existing)
- Handle single video IDs in playlists.yaml (not just playlist IDs)

**Test requirements**:
- Unit test: correct categorization of playlists (media vs other)
- Unit test: single video ID handling
- Integration test: small subset migration with mocked APIs

**Integration**: Uses core library directly. One-time bootstrap tool.

**Demo**: `python scripts/migrate.py --config playlists.yaml --vault-path vault/` populates vault with media notes.

## Step 10: Taskfile and documentation

**Objective**: Create Taskfile.yml for all operations, update README, create vault template files.

**Implementation guidance**:
- Taskfile tasks: `setup`, `lint`, `test`, `migrate`, `serve` (run MCP server for testing)
- Create `vault/queries/by-client.md`, `vault/queries/by-tag.md`, `vault/queries/recent.md` with Dataview queries
- Create `vault/templates/video-note.md` (Obsidian template)
- Update README.md with project description, setup instructions, usage
- Create MCP server config example (for Claude Desktop / Kiro)
- Add `.env.example`

**Test requirements**:
- `task setup` succeeds
- `task lint` passes
- `task test` runs all tests
- Dataview query files have valid syntax

**Integration**: Final polish, makes the project usable.

**Demo**: `task --list` shows all available tasks. README explains setup and usage.
