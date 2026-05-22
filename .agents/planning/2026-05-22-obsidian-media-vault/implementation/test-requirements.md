# Test Requirements — youtube-to-vault
# Organized by Implementation Step

> Each step lists: mapped REQ-IDs, test layers, and acceptance criteria (Given/When/Then).
> All unit tests use mocked external services unless marked `[REAL API]`.
> Integration tests marked `@pytest.mark.integration` require `GOOGLE_API_KEY` + AWS credentials.

---

## Step 1: Project Scaffolding

**REQ-IDs**: NFR-4 (no extra deps), FR-15 (configurable vault path implied by package structure)

**Layers**: UNIT (import smoke test)

### AC-1.1 — Package is importable
- **Given** `uv sync` has completed successfully
- **When** `python -c "import youtube_to_vault"` is executed
- **Then** exit code is 0, no ImportError

### AC-1.2 — All declared dependencies resolve
- **Given** `pyproject.toml` lists fastmcp, youtube-transcript-api, google-api-python-client, boto3, python-frontmatter, pyyaml, tenacity, click
- **When** `uv sync` runs
- **Then** all packages install without conflict, `uv.lock` is generated

### AC-1.3 — No undeclared runtime imports
- **Given** the installed environment
- **When** each core module is imported
- **Then** no `ModuleNotFoundError` for any import in `src/youtube_to_vault/`

---

## Step 2: YouTube Fetcher (`youtube.py`)

**REQ-IDs**: FR-2 (metadata feeds classifier), FR-7 (metadata feeds frontmatter), FR-14 (playlist iteration)

**Layers**: UNIT, INTEGRATION

### AC-2.1 — URL parsing covers all YouTube URL formats [UNIT, PBT]
- **Given** any of: `https://youtu.be/{id}`, `https://www.youtube.com/watch?v={id}`, `https://youtube.com/watch?v={id}&list={pl}`, bare video ID string
- **When** `parse_youtube_url(url)` is called
- **Then** `video_id` equals the expected ID for all variants
- **PBT property**: `parse(parse(url)).video_id == parse(url).video_id` (idempotent)

### AC-2.2 — Playlist URL parsing [UNIT]
- **Given** `https://youtube.com/playlist?list=PL123` or bare `PL123`
- **When** `parse_youtube_url(url)` is called
- **Then** `playlist_id == "PL123"`, `video_id is None`

### AC-2.3 — Video metadata fields populated [UNIT]
- **Given** a mocked YouTube API response with all fields present
- **When** `fetch_video_metadata(video_id)` is called
- **Then** `VideoMetadata` has non-empty `title`, `description`, `published_at`, `channel_title`; `language` equals `defaultAudioLanguage` from response

### AC-2.4 — Missing `defaultAudioLanguage` yields `language=None` [UNIT]
- **Given** a mocked API response without `defaultAudioLanguage`
- **When** `fetch_video_metadata(video_id)` is called
- **Then** `result.language is None`, no exception raised

### AC-2.5 — Playlist pagination collects all videos [UNIT]
- **Given** a mocked API that returns page 1 with `nextPageToken` and page 2 without
- **When** `fetch_playlist_videos(playlist_id)` is called
- **Then** result contains videos from both pages, no duplicates

### AC-2.6 — Empty playlist returns empty list [UNIT]
- **Given** a mocked API returning 0 items
- **When** `fetch_playlist_videos(playlist_id)` is called
- **Then** returns `[]`, no exception

### AC-2.7 — Real API returns valid metadata [INTEGRATION, REAL API]
- **Given** `GOOGLE_API_KEY` is set and network is available
- **When** `fetch_video_metadata("TRma3Bw1hUI")` is called
- **Then** `title` is non-empty, `published_at` parses as ISO 8601 date

---

## Step 3: Transcript Extractor (`transcript.py`)

**REQ-IDs**: FR-4 (language priority), FR-12 (retry on IpBlocked), FR-13 (graceful unavailability)

**Layers**: UNIT, INTEGRATION

### AC-3.1 — Preferred language selected when available [UNIT, PBT]
- **Given** transcripts available in `["en", "fr"]`
- **When** `fetch_transcript(id, ["fr", "en"])` is called
- **Then** `result.language == "fr"`, `result.available == True`
- **PBT property**: if preferred language is in available languages, it is always selected

### AC-3.2 — Fallback to available language when preferred absent [UNIT]
- **Given** only `"en"` transcript available, preferred is `["fr"]`
- **When** `fetch_transcript(id, ["fr"])` is called
- **Then** `result.language == "en"`, `result.available == True`

### AC-3.3 — `TranscriptsDisabled` returns unavailable result [UNIT]
- **Given** `youtube_transcript_api` raises `TranscriptsDisabled`
- **When** `fetch_transcript(id)` is called
- **Then** `result.available == False`, `result.text == ""`, no exception propagated

### AC-3.4 — `NoTranscriptFound` returns unavailable result [UNIT]
- **Given** `youtube_transcript_api` raises `NoTranscriptFound`
- **When** `fetch_transcript(id)` is called
- **Then** `result.available == False`, no exception propagated

### AC-3.5 — `IpBlocked` retries with backoff then returns unavailable [UNIT]
- **Given** `IpBlocked` raised on all retry attempts (max 3)
- **When** `fetch_transcript(id)` is called
- **Then** `result.available == False`, tenacity retried exactly 3 times

### AC-3.6 — `IpBlocked` succeeds on retry [UNIT]
- **Given** `IpBlocked` raised twice, then success on 3rd attempt
- **When** `fetch_transcript(id)` is called
- **Then** `result.available == True`, `result.text` is non-empty

### AC-3.7 — Segments concatenated into single text [UNIT]
- **Given** API returns segments `[{"text": "Hello"}, {"text": "world"}]`
- **When** `fetch_transcript(id)` is called
- **Then** `result.text == "Hello world"` (space-joined)

### AC-3.8 — Real transcript fetch [INTEGRATION, REAL API]
- **Given** network available, video `TRma3Bw1hUI` has a French transcript
- **When** `fetch_transcript("TRma3Bw1hUI", ["fr", "en"])` is called
- **Then** `result.available == True`, `result.text` length > 100, `result.language` in `["fr", "en"]`

---

## Step 4: LLM Classifier (`classifier.py`)

**REQ-IDs**: FR-2 (auto thematic), FR-3a (thematic override — tested in pipeline), FR-3b (low confidence candidates), NFR-3 (title+description only)

**Layers**: UNIT, LLM-EVAL

### AC-4.1 — Known thematic returned when confidence high [UNIT]
- **Given** Bedrock returns `{"thematic": "media", "confidence": 0.95, "candidates": [], "is_media_client": true}`
- **When** `classify_video(metadata, ["media", "ai"])` is called
- **Then** `result.thematic == "media"`, `result.confidence == 0.95`, `result.is_media_client == True`

### AC-4.2 — Low confidence returns candidates, thematic=None [UNIT]
- **Given** Bedrock returns `{"thematic": null, "confidence": 0.4, "candidates": ["media", "ai"], "is_media_client": false}`
- **When** `classify_video(metadata, ["media", "ai"])` is called
- **Then** `result.thematic is None`, `result.candidates == ["media", "ai"]`

### AC-4.3 — Malformed JSON response handled gracefully [UNIT]
- **Given** Bedrock returns a non-JSON string
- **When** `classify_video(metadata, [])` is called
- **Then** `result.thematic is None`, no exception raised

### AC-4.4 — ThrottlingException triggers retry [UNIT]
- **Given** Bedrock raises `ThrottlingException` twice, then returns valid JSON
- **When** `classify_video(metadata, [])` is called
- **Then** result is valid, tenacity retried

### AC-4.5 — Only title and description sent to Bedrock [UNIT, NFR-3]
- **Given** a `VideoMetadata` with title, description, and a separate transcript string
- **When** `classify_video(metadata, [])` is called (transcript NOT a parameter)
- **Then** the Bedrock request body contains title and description but NOT transcript text

### AC-4.6 — Client detection returns list of names [UNIT]
- **Given** Bedrock returns `["TF1", "Canal+"]`
- **When** `detect_clients(metadata, transcript)` is called
- **Then** result == `["TF1", "Canal+"]`

### AC-4.7 — Confidence is always in [0.0, 1.0] [UNIT, PBT]
- **PBT property**: for any valid Bedrock response, `0.0 <= result.confidence <= 1.0`

### AC-4.8 — Classification accuracy on labeled videos [LLM-EVAL]
- **Given** 10 labeled videos (5 media, 5 non-media) from `tests/fixtures/labeled_videos.json`
- **When** `classify_video` is called for each (real Bedrock)
- **Then** ≥ 8/10 correct classifications (80% accuracy threshold)
- **Sampling**: 2 runs per video; pass if both agree

---

## Step 5: AI Summarizer (`summarizer.py`)

**REQ-IDs**: FR-5 (Bedrock summary), FR-6 (format rules), FR-13a (description fallback)

**Layers**: UNIT, LLM-EVAL

### AC-5.1 — Summary returned from mocked Bedrock [UNIT]
- **Given** Bedrock returns a markdown string
- **When** `generate_summary(transcript, description, metadata, "fr")` is called
- **Then** return value equals the mocked response string

### AC-5.2 — Description-only path omits transcript from prompt [UNIT]
- **Given** `transcript=None`
- **When** `generate_summary(None, description, metadata, "en")` is called
- **Then** the Bedrock request does NOT include a transcript section in the user message

### AC-5.3 — Language instruction included in prompt [UNIT]
- **Given** `language="fr"`
- **When** `generate_summary(...)` is called
- **Then** the system prompt or user message contains a language instruction referencing "fr" or "français"

### AC-5.4 — Bedrock called with correct parameters [UNIT]
- **Given** any valid inputs
- **When** `generate_summary(...)` is called
- **Then** Bedrock Converse called with `maxTokens=4096`, `temperature=0.3`

### AC-5.5 — ThrottlingException triggers retry [UNIT]
- **Given** Bedrock raises `ThrottlingException` twice, then succeeds
- **When** `generate_summary(...)` is called
- **Then** summary returned, tenacity retried

### AC-5.6 — Summary format compliance [LLM-EVAL]
- **Given** 5 videos with French transcripts (real Bedrock)
- **When** `generate_summary(...)` is called for each
- **Then** ALL of the following hold for each output:
  - Zero `- ` or `* ` list items (exact check)
  - `#`, `##`, `###` all present; no `####` (regex check)
  - `langdetect(output) == "fr"` (library check)
  - LLM judge rates formality ≥ 4/5 using rubric from FR-6
- **Sampling**: 3 runs per video; pass if ≥ 2/3 pass all criteria

---

## Step 6: Vault Writer (`vault.py`)

**REQ-IDs**: FR-7 (frontmatter), FR-8 (wikilinks), FR-9 (MOC), FR-10 (query pages), FR-11 (idempotency), FR-15 (configurable path)

**Layers**: UNIT

All tests use `tmp_path` pytest fixture.

### AC-6.1 — Note file created at correct path [UNIT]
- **Given** `write_note(metadata, summary, clients, tags, thematic="media")`
- **When** called with `year=2023`, `playlist="media-symposium"`
- **Then** file exists at `{vault}/media/2023/media-symposium/{slug}.md`

### AC-6.2 — Frontmatter contains all 12 required fields [UNIT]
- **Given** a written note
- **When** frontmatter is parsed with `python-frontmatter`
- **Then** all fields present: `title`, `description`, `event`, `year`, `clients`, `tags`, `url`, `date`, `language`, `has_transcript`, `thematic`, `playlist`

### AC-6.3 — Frontmatter field types are correct [UNIT, PBT]
- **PBT property**: for any valid `VideoMetadata`, `year` is int, `clients` is list, `has_transcript` is bool, `date` parses as date
- **Then** no type errors when parsing frontmatter

### AC-6.4 — Client names rendered as wikilinks [UNIT]
- **Given** `clients=["TF1", "Canal+"]`
- **When** note body is read
- **Then** body contains `[[TF1]]` and `[[Canal+]]`

### AC-6.5 — `note_exists` returns True after write [UNIT]
- **Given** a note written for `video_id="ABC123"`
- **When** `note_exists("ABC123")` is called
- **Then** returns `True`

### AC-6.6 — `note_exists` returns False for unknown video [UNIT]
- **Given** empty vault
- **When** `note_exists("UNKNOWN")` is called
- **Then** returns `False`

### AC-6.7 — `note_exists` is idempotent [UNIT, PBT]
- **PBT property**: `note_exists(id) == note_exists(id)` for any `id`

### AC-6.8 — `update_moc` creates `_index.md` [UNIT]
- **Given** no existing `_index.md`
- **When** `update_moc("media", 2023, "media-symposium")` is called
- **Then** `{vault}/media/2023/media-symposium/_index.md` exists with a link to the playlist

### AC-6.9 — `update_moc` does not duplicate entries [UNIT]
- **Given** `_index.md` already contains an entry for "media-symposium"
- **When** `update_moc("media", 2023, "media-symposium")` is called again
- **Then** `_index.md` contains exactly one entry for "media-symposium"

### AC-6.10 — `get_existing_thematics` excludes system directories [UNIT]
- **Given** vault contains dirs: `media/`, `ai/`, `queries/`, `templates/`
- **When** `get_existing_thematics()` is called
- **Then** returns `["media", "ai"]` (or equivalent set), NOT `["queries", "templates"]`

### AC-6.11 — Vault path is configurable [UNIT]
- **Given** `VaultWriter(VaultConfig(vault_path=custom_path))`
- **When** any write operation is performed
- **Then** all files are created under `custom_path`, not a default path

### AC-6.12 — Title with YAML special characters is handled [UNIT]
- **Given** `title = 'Video: "AWS" #1'`
- **When** note is written and frontmatter parsed
- **Then** no YAML parse error, `title` field equals original string

---

## Step 7: Pipeline Orchestrator (`pipeline.py`)

**REQ-IDs**: FR-11 (idempotency), FR-3a (thematic override), FR-3b (low confidence), FR-12 (retry — delegated to components), NFR-2 (error isolation)

**Layers**: UNIT, INTEGRATION

All unit tests mock all 5 dependencies (youtube, transcript, classifier, summarizer, vault).

### AC-7.1 — Full pipeline produces "created" result [UNIT]
- **Given** all dependencies succeed, `note_exists` returns False
- **When** `process_video(video_id, config, thematic="media")` is called
- **Then** `result.status == "created"`, `result.note_path` is not None, `result.error is None`

### AC-7.2 — Existing note is skipped [UNIT]
- **Given** `note_exists` returns True
- **When** `process_video(video_id, config)` is called
- **Then** `result.status == "skipped"`, no downstream calls to transcript/classifier/summarizer/vault_write

### AC-7.3 — Thematic override skips classifier [UNIT]
- **Given** `thematic="media"` provided
- **When** `process_video(video_id, config, thematic="media")` is called
- **Then** `classify_video` is NOT called

### AC-7.4 — Low confidence classification returns error with candidates [UNIT]
- **Given** no thematic provided, classifier returns `confidence < threshold`, `thematic=None`, `candidates=["media", "ai"]`
- **When** `process_video(video_id, config)` is called
- **Then** `result.status == "error"`, `result.error` contains the candidate list

### AC-7.5 — Transcript unavailability falls back to description [UNIT]
- **Given** `transcript.available == False`
- **When** `process_video(video_id, config, thematic="media")` is called
- **Then** `summarizer.generate_summary` called with `transcript=None`, pipeline continues to completion

### AC-7.6 — One video failure does not block others [UNIT, NFR-2]
- **Given** a playlist of 3 videos where video 2 raises an unhandled exception
- **When** `process_playlist(playlist_id, config, thematic="media")` is called
- **Then** returns 3 results; video 2 has `status == "error"`; videos 1 and 3 have `status == "created"`

### AC-7.7 — `existing_thematics` passed to classifier [UNIT]
- **Given** vault has existing thematics `["media", "ai"]`
- **When** `process_video(video_id, config)` is called without thematic
- **Then** `classify_video` receives `existing_thematics=["media", "ai"]`

### AC-7.8 — Result count equals input video count [UNIT, PBT]
- **PBT property**: `len(process_playlist(id, config)) == len(fetch_playlist_videos(id))`

### AC-7.9 — All result statuses are valid [UNIT, PBT]
- **PBT property**: for any result in `process_playlist(...)`, `result.status in {"created", "skipped", "error"}`

### AC-7.10 — Full pipeline integration with real YouTube API [INTEGRATION, REAL API]
- **Given** `GOOGLE_API_KEY` set, Bedrock mocked, tmp vault
- **When** `process_video("TRma3Bw1hUI", config, thematic="media")` is called
- **Then** note file created, frontmatter valid, second call returns `status == "skipped"`

---

## Step 8: MCP Server (`server.py`)

**REQ-IDs**: FR-1 (tools exposed), FR-15 (vault path from env/param)

**Layers**: UNIT, INTEGRATION, CONTRACT

### AC-8.1 — All three tools are registered [UNIT]
- **Given** server is instantiated
- **When** tool list is queried via FastMCP introspection
- **Then** `add_video`, `add_playlist`, `list_thematics` are all present

### AC-8.2 — Tool schemas match contract snapshot [CONTRACT]
- **Given** `tests/fixtures/tool_schemas.json` exists
- **When** server tool schemas are captured at runtime
- **Then** schemas match snapshot exactly (parameter names, types, required fields)

### AC-8.3 — `add_video` parses URL and delegates to pipeline [UNIT]
- **Given** pipeline mocked, `vault_path` provided
- **When** `add_video("https://youtu.be/ABC123", thematic="media", vault_path="/tmp/vault")` is called
- **Then** `process_video("ABC123", ...)` called with correct video ID

### AC-8.4 — `add_playlist` parses URL and delegates to pipeline [UNIT]
- **Given** pipeline mocked
- **When** `add_playlist("https://youtube.com/playlist?list=PL123", thematic="media")` is called
- **Then** `process_playlist("PL123", ...)` called

### AC-8.5 — Default vault path from environment variable [UNIT]
- **Given** `VAULT_PATH` env var set to `/tmp/test-vault`, no `vault_path` param
- **When** any tool is called without `vault_path`
- **Then** pipeline called with vault path from env var

### AC-8.6 — `list_thematics` returns vault directories [UNIT]
- **Given** vault has `media/` and `ai/` directories
- **When** `list_thematics(vault_path=tmp_vault)` is called
- **Then** returns list containing `"media"` and `"ai"`

### AC-8.7 — Tool invocation via FastMCP test client [INTEGRATION]
- **Given** FastMCP test client, pipeline mocked
- **When** `add_video` tool is invoked via MCP protocol
- **Then** response is a dict with `status` key, no MCP protocol errors

---

## Step 9: Migration Script (`scripts/migrate.py`)

**REQ-IDs**: FR-14 (media vs other categorization), FR-11 (idempotency via pipeline)

**Layers**: UNIT, INTEGRATION

### AC-9.1 — Media playlists correctly categorized [UNIT]
- **Given** `playlists.yaml` with categories: `media-symposium`, `ibc`, `nab`, `media-day`
- **When** categorization logic runs
- **Then** all four are classified as `is_media=True`

### AC-9.2 — Non-media playlists correctly categorized [UNIT]
- **Given** `playlists.yaml` with categories: `reinvent`, `security`, `devops`
- **When** categorization logic runs
- **Then** all three are classified as `is_media=False`

### AC-9.3 — Single video ID handled (not playlist) [UNIT]
- **Given** a `playlists.yaml` entry with a `video_id` field instead of `playlist_id`
- **When** migration processes that entry
- **Then** `process_video` is called (not `process_playlist`)

### AC-9.4 — Non-media videos filtered by `is_media_client` [UNIT]
- **Given** a non-media playlist with 3 videos; classifier returns `is_media_client=True` for 1, `False` for 2
- **When** migration processes that playlist
- **Then** only 1 video is processed through the full pipeline

### AC-9.5 — Resume via idempotency [UNIT]
- **Given** all notes already exist (`note_exists` returns True for all)
- **When** migration runs
- **Then** no new notes written, exit code 0, no errors

### AC-9.6 — Progress reported to stdout [UNIT]
- **Given** a playlist with 3 videos (2 created, 1 error)
- **When** migration runs
- **Then** stdout contains counts: created=2, error=1

### AC-9.7 — CLI accepts required arguments [UNIT]
- **Given** `--config` and `--vault-path` arguments
- **When** `python scripts/migrate.py --config playlists.yaml --vault-path /tmp/vault` is invoked
- **Then** exit code 0 (with mocked pipeline)

### AC-9.8 — Small subset migration [INTEGRATION, REAL API]
- **Given** real `playlists.yaml`, `GOOGLE_API_KEY` set, Bedrock mocked, tmp vault, `--limit 2`
- **When** migration script runs
- **Then** ≤ 2 notes created or skipped, exit code 0, no unhandled exceptions

---

## Step 10: Taskfile and Documentation

**REQ-IDs**: FR-10 (Dataview query pages), NFR-4 (no extra deps implied by clean setup)

**Layers**: UNIT (file content validation)

### AC-10.1 — `task setup` succeeds [UNIT]
- **Given** clean environment with uv installed
- **When** `task setup` runs
- **Then** exit code 0, `.venv` created, all deps installed

### AC-10.2 — `task lint` passes on clean codebase [UNIT]
- **Given** freshly scaffolded code
- **When** `task lint` runs
- **Then** exit code 0, no ruff errors

### AC-10.3 — `task test` runs all unit tests [UNIT]
- **When** `task test` runs
- **Then** exit code 0, all unit tests pass, integration tests excluded

### AC-10.4 — Dataview query files have valid syntax [UNIT]
- **Given** `vault/queries/by-client.md`, `vault/queries/by-tag.md`, `vault/queries/recent.md`
- **When** each file is read
- **Then** each contains a fenced `dataview` code block with valid Dataview query syntax (FROM, WHERE, SORT keywords present)

### AC-10.5 — `task --list` shows all expected tasks [UNIT]
- **When** `task --list` runs
- **Then** output contains: `setup`, `lint`, `test`, `migrate`, `serve`
