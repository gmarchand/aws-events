# QA Test Plan Annex — youtube-to-vault

> This annex is appended to `detailed-design.md` without modifying the original content.
> Generated: 2026-05-22

---

## Phase 1.1 — Requirement Extraction (EARS Format)

### Functional Requirements

| ID | EARS Statement | Layers | INCOSE Quality |
|----|---------------|--------|----------------|
| FR-1 | WHEN an MCP client calls `add_video` or `add_playlist`, THE SYSTEM SHALL expose those tools and return a structured result | UNIT, INTEGRATION, E2E | OK |
| FR-2 | WHEN a video is processed without a `thematic` parameter, THE SYSTEM SHALL classify the thematic from title and description via LLM | UNIT, INTEGRATION | OK |
| FR-3 | WHEN a `thematic` parameter is provided, THE SYSTEM SHALL use it without calling the classifier; WHEN classification confidence is below threshold, THE SYSTEM SHALL return candidate thematics instead of writing a note | UNIT | Violation: compound (two behaviors) |
| FR-4 | WHEN a transcript is requested, THE SYSTEM SHALL fetch it via `youtube-transcript-api` using the video's language as first priority, then `['fr', 'en']` as fallback | UNIT | OK |
| FR-5 | WHEN a transcript or description is available, THE SYSTEM SHALL generate a summary via Bedrock Claude Opus 4 in the video's detected language | UNIT, INTEGRATION | OK |
| FR-6 | WHEN generating a summary, THE SYSTEM SHALL produce active-voice flowing paragraphs with exactly 3 heading levels, formal tone, and no bullet points | LLM-EVAL | Violation: not fully verifiable by exact comparison |
| FR-7 | WHEN writing a note, THE SYSTEM SHALL include frontmatter with all required fields: title, description, event, year, clients, tags, url, date, language, has_transcript, thematic, playlist | UNIT | OK |
| FR-8 | WHEN writing a note body, THE SYSTEM SHALL render client names as wikilinks (`[[ClientName]]`) | UNIT | OK |
| FR-9 | WHEN a note is written, THE SYSTEM SHALL create or update the event MOC (`_index.md`) and the root `MOC.md` | UNIT | OK |
| FR-10 | WHEN the vault is initialized, THE SYSTEM SHALL create Dataview query pages for by-client, by-tag, and recent views | UNIT | OK |
| FR-11 | WHEN a video has already been processed (note exists), THE SYSTEM SHALL skip it without error | UNIT | OK |
| FR-12 | WHEN a transient error occurs (IpBlocked, Bedrock ThrottlingException), THE SYSTEM SHALL retry with exponential backoff | UNIT | OK |
| FR-13 | WHEN no transcript is available, THE SYSTEM SHALL summarize from description; WHEN description is insufficient, THE SYSTEM SHALL create the note without a summary | UNIT | Violation: compound |
| FR-14 | WHEN the migration script runs, THE SYSTEM SHALL process all videos in media playlists with `thematic="media"` and classify-then-filter videos in other playlists | UNIT, INTEGRATION | OK |
| FR-15 | WHEN a vault path is provided as a server parameter or environment variable, THE SYSTEM SHALL use it as the root for all vault operations | UNIT | OK |

### Non-Functional Requirements

| ID | EARS Statement | Layers | INCOSE Quality |
|----|---------------|--------|----------------|
| NFR-1 | WHEN processing a single video (excluding Bedrock latency), THE SYSTEM SHALL complete within 60 seconds | INTEGRATION | Violation: "excluding Bedrock latency" makes it hard to measure in practice |
| NFR-2 | WHEN one video in a playlist fails, THE SYSTEM SHALL continue processing remaining videos and report the failure | UNIT | OK |
| NFR-3 | WHEN classifying a video, THE SYSTEM SHALL send only title and description to the LLM (not the full transcript) | UNIT | OK |
| NFR-4 | THE SYSTEM SHALL have no runtime dependencies beyond YouTube Data API v3, youtube-transcript-api, and Amazon Bedrock | UNIT | OK |

---

## Phase 1.2 — Processing Strategy

19 requirements total (15 FR + 4 NFR). Single-pass processing applies (≤ 30 requirements).

Priority tiers:
- **Critical**: FR-1, FR-7, FR-11, FR-12, NFR-2 — core correctness and reliability
- **High**: FR-4, FR-5, FR-6, FR-13, FR-14 — primary data pipeline
- **Medium**: FR-2, FR-3, FR-8, FR-9, FR-15 — enrichment and structure
- **Low**: FR-10, NFR-1, NFR-3, NFR-4 — polish and constraints

---

## Phase 1.3 — Coverage Matrix

| REQ-ID | EARS (short) | Layer(s) | Priority | Status | Test Status |
|--------|-------------|----------|----------|--------|-------------|
| FR-1 | MCP tools exposed | UNIT, INTEGRATION, E2E | Critical | Not Implemented | To Do |
| FR-2 | Auto thematic classification | UNIT, INTEGRATION | High | Not Implemented | To Do |
| FR-3a | Thematic override skips classifier | UNIT | Medium | Not Implemented | To Do |
| FR-3b | Low confidence returns candidates | UNIT | Medium | Not Implemented | To Do |
| FR-4 | Transcript fetch with language priority | UNIT | High | Not Implemented | To Do |
| FR-5 | Summary via Bedrock in video language | UNIT, INTEGRATION | High | Not Implemented | To Do |
| FR-6 | Summary format rules | LLM-EVAL | High | Not Implemented | To Do |
| FR-7 | Frontmatter completeness | UNIT | Critical | Not Implemented | To Do |
| FR-8 | Wikilinks in note body | UNIT | Medium | Not Implemented | To Do |
| FR-9 | MOC creation/update | UNIT | Medium | Not Implemented | To Do |
| FR-10 | Dataview query pages | UNIT | Low | Not Implemented | To Do |
| FR-11 | Idempotency | UNIT | Critical | Not Implemented | To Do |
| FR-12 | Retry with backoff | UNIT | Critical | Not Implemented | To Do |
| FR-13a | Fallback to description summary | UNIT | High | Not Implemented | To Do |
| FR-13b | Note without summary when description insufficient | UNIT | High | Not Implemented | To Do |
| FR-14 | Migration script categorization | UNIT, INTEGRATION | High | Not Implemented | To Do |
| FR-15 | Configurable vault path | UNIT | Medium | Not Implemented | To Do |
| NFR-1 | Single video < 60s | INTEGRATION | Low | Not Implemented | To Do |
| NFR-2 | Graceful degradation | UNIT | Critical | Not Implemented | To Do |
| NFR-3 | Classification uses title+description only | UNIT | Low | Not Implemented | To Do |
| NFR-4 | No extra runtime deps | UNIT | Low | Not Implemented | To Do |

---

## Phase 2 — Unit Test Plan `[UNIT]`

### `youtube.py`

**REQ**: FR-2 (metadata feeds classifier), FR-7 (metadata feeds frontmatter), NFR-4

**Properties (PBT)**:
- `parse_youtube_url(url)` is idempotent: `parse(parse(url)) == parse(url)`
- For any valid video ID string `v`, `parse_youtube_url(f"https://youtu.be/{v}").video_id == v`
- For any valid playlist ID `p`, `parse_youtube_url(f"https://youtube.com/playlist?list={p}").playlist_id == p`

**Test cases**:
```
test_parse_url_variants:
  inputs: ["https://youtu.be/ABC", "https://www.youtube.com/watch?v=ABC",
           "https://youtube.com/watch?v=ABC&list=PL123", "ABC"]
  assert: video_id == "ABC" for all

test_parse_playlist_url:
  inputs: ["https://youtube.com/playlist?list=PL123", "PL123"]
  assert: playlist_id == "PL123"

test_fetch_video_metadata_mocked:
  mock: YouTube API returns fixture response
  assert: VideoMetadata fields populated correctly, language extracted from defaultAudioLanguage

test_fetch_playlist_videos_pagination:
  mock: API returns 2 pages (nextPageToken present on first)
  assert: all videos from both pages returned, no duplicates

test_fetch_video_missing:
  mock: API returns empty items list
  assert: raises ValueError or returns None (per design decision)
```

**Adversarial cases**:
- URL with extra query params (`&t=30s`)
- Video ID with special characters (should be rejected)
- Playlist with 0 videos
- `defaultAudioLanguage` absent → `language=None`

---

### `transcript.py`

**REQ**: FR-4, FR-12, FR-13

**Properties (PBT)**:
- For any `preferred_languages` list, if the video has a transcript in any listed language, `result.language` is in `preferred_languages`
- `fetch_transcript` never raises — always returns `TranscriptResult`
- `result.available == False` implies `result.text == ""`

**Test cases**:
```
test_language_priority_exact_match:
  mock: transcripts available in ["en", "fr"]
  call: fetch_transcript(id, ["fr", "en"])
  assert: result.language == "fr"

test_language_fallback:
  mock: only "en" available
  call: fetch_transcript(id, ["fr"])
  assert: result.language == "en", result.available == True

test_transcripts_disabled:
  mock: raises TranscriptsDisabled
  assert: result.available == False, no exception raised

test_no_transcript_found:
  mock: raises NoTranscriptFound
  assert: result.available == False

test_ip_blocked_retry:
  mock: raises IpBlocked twice, then succeeds on 3rd attempt
  assert: result.available == True, tenacity retried exactly 2 times

test_ip_blocked_exhausted:
  mock: raises IpBlocked on all 3 attempts
  assert: result.available == False

test_segment_concatenation:
  mock: returns 3 segments ["Hello", "world", "foo"]
  assert: result.text == "Hello world foo"
```

---

### `classifier.py`

**REQ**: FR-2, FR-3, NFR-3

**Properties (PBT)**:
- `classify_video` never sends transcript text to Bedrock (only title+description)
- `result.confidence` is always in [0.0, 1.0]
- If `existing_thematics` is non-empty, `result.thematic` is either in `existing_thematics` or `None`

**Test cases**:
```
test_classify_returns_known_thematic:
  mock: Bedrock returns {"thematic": "media", "confidence": 0.95, "candidates": [], "is_media_client": true}
  assert: result.thematic == "media", result.confidence == 0.95

test_classify_low_confidence_returns_candidates:
  mock: Bedrock returns {"thematic": null, "confidence": 0.4, "candidates": ["media", "ai"], "is_media_client": false}
  assert: result.thematic is None, result.candidates == ["media", "ai"]

test_classify_malformed_json:
  mock: Bedrock returns non-JSON text
  assert: result.thematic is None, no exception raised

test_classify_throttling_retry:
  mock: ThrottlingException twice, then valid response
  assert: result.thematic is not None, retried

test_detect_clients_extracts_names:
  mock: Bedrock returns ["TF1", "Canal+"]
  assert: result == ["TF1", "Canal+"]

test_classify_only_uses_title_description:
  spy: capture Bedrock request body
  assert: request body does NOT contain transcript text
```

---

### `summarizer.py`

**REQ**: FR-5, FR-6, FR-13

**Properties (PBT)**:
- `generate_summary` with `transcript=None` produces shorter output than with transcript (statistical, not exact)
- Language instruction appears in the prompt for any non-English language

**Test cases**:
```
test_summary_with_transcript:
  mock: Bedrock returns markdown string
  assert: return value equals mocked response

test_summary_description_only:
  mock: transcript=None, Bedrock returns shorter markdown
  assert: prompt sent to Bedrock does NOT include transcript section

test_language_in_prompt:
  spy: capture prompt
  call: generate_summary(..., language="fr")
  assert: "fr" or "français" appears in system prompt or user message

test_throttling_retry:
  mock: ThrottlingException x2, then success
  assert: summary returned, retried

test_maxTokens_and_temperature:
  spy: capture Bedrock Converse call params
  assert: maxTokens == 4096, temperature == 0.3
```

---

### `vault.py`

**REQ**: FR-7, FR-8, FR-9, FR-10, FR-11, FR-15

**Properties (PBT)**:
- `slugify(title)` produces only lowercase alphanumeric and hyphens
- `note_exists(video_id)` is idempotent: calling it twice returns the same result
- `write_note` followed by `note_exists(same_video_id)` always returns `True`

**Test cases** (all use `tmp_path` fixture):
```
test_write_note_creates_file:
  assert: file exists at thematic/year/playlist/slug.md

test_write_note_frontmatter_complete:
  parse frontmatter of written file
  assert: all 12 required fields present and correctly typed

test_write_note_wikilinks:
  call: write_note(..., clients=["TF1", "Canal+"])
  assert: note body contains "[[TF1]]" and "[[Canal+]]"

test_note_exists_true:
  write a note, then call note_exists(same_video_id)
  assert: True

test_note_exists_false:
  call note_exists on empty vault
  assert: False

test_note_exists_idempotent:
  assert: note_exists(id) == note_exists(id)

test_update_moc_creates_index:
  call update_moc("media", 2023, "media-symposium")
  assert: vault/media/2023/media-symposium/_index.md created with link to playlist

test_update_moc_appends_new_entry:
  create _index.md with one entry, call update_moc again with new playlist
  assert: both entries present, no duplicates

test_get_existing_thematics_excludes_system_dirs:
  create dirs: media/, queries/, templates/, ai/
  assert: returns ["media", "ai"], not ["queries", "templates"]

test_vault_path_configurable:
  create VaultWriter with custom path
  assert: all writes go to that path
```

---

### `pipeline.py`

**REQ**: FR-11, FR-12, NFR-2, FR-3a, FR-3b

**Properties (PBT)**:
- `process_playlist` result count equals input video count
- All results have `status` in `{"created", "skipped", "error"}`
- If `note_exists` returns True, result status is always `"skipped"`

**Test cases** (all dependencies mocked):
```
test_process_video_full_pipeline:
  mock: all dependencies succeed
  assert: result.status == "created", result.note_path is not None

test_process_video_idempotent:
  mock: note_exists returns True
  assert: result.status == "skipped", no downstream calls made

test_process_video_thematic_override:
  call: process_video(..., thematic="media")
  assert: classifier NOT called

test_process_video_classification_low_confidence:
  mock: classifier returns confidence < threshold, thematic=None
  assert: result.status == "error", result.error contains candidates

test_process_video_transcript_error_continues:
  mock: transcript fetch returns available=False
  assert: pipeline continues to summarizer with description fallback

test_process_playlist_error_isolation:
  mock: video 2 of 3 raises exception
  assert: results has 3 entries, video 2 status == "error", videos 1 and 3 status == "created"

test_process_playlist_passes_existing_thematics:
  spy: capture classifier call args
  assert: existing_thematics from vault writer passed to classifier
```

---

### `migrate.py`

**REQ**: FR-14

**Test cases**:
```
test_categorize_media_playlists:
  input: playlists.yaml with "media-symposium", "ibc", "nab", "media-day" categories
  assert: all categorized as media=True

test_categorize_other_playlists:
  input: playlists.yaml with "reinvent", "security" categories
  assert: categorized as media=False

test_single_video_id_handling:
  input: playlists.yaml entry with video_id instead of playlist_id
  assert: process_video called (not process_playlist)

test_resume_via_idempotency:
  mock: note_exists returns True for all
  assert: no new notes written, no errors
```

---

## Phase 3 — Integration Test Plan `[INTEGRATION]`

> **Policy**: Integration tests hit real AWS services (Bedrock) and real YouTube APIs. They require `GOOGLE_API_KEY` and valid AWS credentials with Bedrock access. Tests are marked `@pytest.mark.integration` and excluded from the default `task test` run. Run via `task test:integration`.

### INT-1: YouTube Fetcher — Real API

**REQ**: FR-2, FR-7  
**Pre-state**: `GOOGLE_API_KEY` set, network available  
**Steps**:
1. Call `fetch_video_metadata("TRma3Bw1hUI")` (known public video)
2. Call `fetch_playlist_videos("PLL_L4MF1Z7JWsJi_LUyEMpLaUirkIz2Do")` (small test playlist)

**Post-state assertions**:
- `VideoMetadata.title` is non-empty string
- `VideoMetadata.published_at` parses as ISO date
- Playlist returns ≥ 1 video

**Failure scenarios**:
- Invalid API key → `HttpError 403` — test asserts error is raised with clear message
- Non-existent video ID → test asserts `ValueError` or empty result

---

### INT-2: Transcript Extractor — Real API

**REQ**: FR-4  
**Pre-state**: Network available (no API key needed)  
**Steps**:
1. Call `fetch_transcript("TRma3Bw1hUI", ["fr", "en"])` on a known video with French transcript

**Post-state assertions**:
- `result.available == True`
- `result.text` length > 100 characters
- `result.language` in `["fr", "en"]`

**Failure scenario**:
- Video with no transcript → `result.available == False`, no exception

---

### INT-3: Full Pipeline — Single Video (Mocked Bedrock)

**REQ**: FR-1 through FR-13, NFR-2  
**Pre-state**: `GOOGLE_API_KEY` set, Bedrock mocked (to avoid cost in CI)  
**Steps**:
1. Call `process_video("TRma3Bw1hUI", vault_config, thematic="media")` with tmp vault

**Post-state assertions**:
- Note file created at correct path
- Frontmatter parses correctly with all required fields
- `note_exists("TRma3Bw1hUI")` returns True
- Second call returns `status == "skipped"`

---

### INT-4: MCP Server Tool Invocation

**REQ**: FR-1, FR-15  
**Pre-state**: FastMCP test client available  
**Steps**:
1. Instantiate server with test vault path
2. Call `list_thematics` tool
3. Call `add_video` with a YouTube URL (pipeline mocked)

**Post-state assertions**:
- `list_thematics` returns a list (possibly empty)
- `add_video` returns a dict with `status` key
- Tool schemas discoverable via MCP protocol

---

## Phase 3b — Contract Test Plan `[CONTRACT]`

This project has one significant interface contract: the **Bedrock Converse API request/response schema** consumed by `classifier.py` and `summarizer.py`.

### CONTRACT-1: Classifier ↔ Bedrock

**Consumer**: `classifier.py`  
**Provider**: Amazon Bedrock Converse API  
**Contract**:
```json
{
  "request": {
    "modelId": "string (Claude Opus 4 ARN)",
    "messages": [{"role": "user", "content": [{"text": "string"}]}],
    "system": [{"text": "string"}],
    "inferenceConfig": {"maxTokens": "integer", "temperature": "float"}
  },
  "response_schema": {
    "thematic": "string | null",
    "confidence": "float [0,1]",
    "candidates": "list[string]",
    "is_media_client": "boolean"
  }
}
```

**Test**: Parse the JSON response from any Bedrock call and validate against this schema. If Bedrock changes its response format, this test catches it.

### CONTRACT-2: Summarizer ↔ Bedrock

**Consumer**: `summarizer.py`  
**Contract**: Response is a plain markdown string (not JSON). Test asserts response is non-empty string and contains at least one `#` heading.

### CONTRACT-3: MCP Tool Schema

**Consumer**: MCP clients (Claude Desktop, Kiro)  
**Contract**: Tool schemas must remain stable. Test captures tool schemas at registration time and compares against a stored snapshot (`tests/fixtures/tool_schemas.json`). Any change to parameter names or types fails the test.

---

## Phase 4 — LLM Evaluation Plan `[LLM-EVAL]`

### EVAL-1: Summary Format Compliance (FR-6)

**Rubric** (derived directly from FR-6 wording):

| Criterion | Pass Condition | Evaluator Type |
|-----------|---------------|----------------|
| Active voice | ≥ 90% of sentences use active voice | Output-level (regex + LLM judge) |
| No bullet points | Zero `- ` or `* ` list items in output | Output-level (exact) |
| Exactly 3 heading levels | `#`, `##`, `###` all present; no `####` | Output-level (regex) |
| Formal tone | LLM judge rates formality ≥ 4/5 | Output-level (LLM judge) |
| Language match | `langdetect(output) == metadata.language` | Output-level (library) |
| Flowing paragraphs | No single-sentence paragraphs; avg paragraph ≥ 3 sentences | Output-level (heuristic) |

**Test cases**:
- 5 videos with French transcripts → assert all 6 criteria pass
- 3 videos with English transcripts → assert language match
- 2 videos with description-only (no transcript) → assert shorter but still format-compliant

**Sampling**: 3 runs per test case, pass if ≥ 2/3 runs pass all criteria.

**Pass threshold**: 100% of format criteria must pass (these are deterministic rules, not quality judgments).

### EVAL-2: Classification Accuracy (FR-2)

**Rubric**:

| Criterion | Pass Condition |
|-----------|---------------|
| Known media video classified as "media" | result.thematic == "media" |
| Non-media video not classified as "media" | result.thematic != "media" OR result.confidence < 0.7 |
| Client detection accuracy | ≥ 80% precision on known client list |

**Test cases**: 10 labeled videos (5 media, 5 non-media) from `playlists.yaml`.

**Sampling**: 2 runs per video (classification is low-variance), pass if both agree.

---

## Phase 4b — End-to-End Test Plan `[E2E]`

Exactly 2 E2E tests. Both require deployed infrastructure (real YouTube API + real Bedrock).

### E2E-1: Add Video via MCP Tool

**Journey**: MCP client → `add_video(url)` → note appears in vault

**Preconditions**: Server running, vault path set, AWS credentials valid, `GOOGLE_API_KEY` set

**Steps**:
1. Call `add_video("https://www.youtube.com/watch?v=TRma3Bw1hUI", thematic="media", vault_path=tmp_vault)`
2. Wait for completion (timeout: 120s)

**Final assertions**:
- Note file exists in `tmp_vault/media/`
- Frontmatter parses without error
- `has_transcript` field is boolean
- Calling `add_video` again with same URL returns `status == "skipped"`

**Flakiness mitigation**: Retry up to 2 times on network errors. Use a stable, public, non-deleted video.

**Justification**: Cannot be covered at lower layers — requires real YouTube API + real Bedrock + real vault write in sequence.

---

### E2E-2: Migration Script — Small Subset

**Journey**: `migrate.py` → processes 2 known videos from `playlists.yaml` → vault populated

**Preconditions**: Same as E2E-1, plus `playlists.yaml` present

**Steps**:
1. Run `python scripts/migrate.py --config playlists.yaml --vault-path tmp_vault --limit 2`
2. Check output

**Final assertions**:
- 2 note files created (or skipped if already exist)
- Exit code 0
- No unhandled exceptions in stderr

**Flakiness mitigation**: `--limit 2` flag keeps runtime bounded. Idempotency means re-runs are safe.

---

## Phase 5 — CI/CD Pipeline Placement

```
┌─────────────────────────────────────────────────────────────┐
│ Every commit (task test)                                     │
│  • All [UNIT] tests                                         │
│  • CONTRACT-3 (tool schema snapshot)                        │
│  • Lint (ruff)                                              │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ Pull Request (task test:integration)                        │
│  • INT-1, INT-2 (real YouTube API, read-only)               │
│  • INT-3 (pipeline with mocked Bedrock)                     │
│  • INT-4 (MCP server tool invocation)                       │
│  • CONTRACT-1, CONTRACT-2 (Bedrock schema validation)       │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ Pre-merge / Manual (task test:e2e)                          │
│  • EVAL-1, EVAL-2 (LLM evaluations, real Bedrock)          │
│  • E2E-1, E2E-2 (full journeys)                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Phase 6 — Spec Gap Report

**Current implementation status**: 0 of 19 requirements implemented (project not yet built).

All requirements are **Blocked** pending implementation. No false coverage claims.

**INCOSE violations to fix before implementation**:
- FR-3: Split into FR-3a (thematic override) and FR-3b (low confidence candidates)
- FR-6: Add measurable criteria (e.g., "no list items", "3 heading levels") — partially addressed in EVAL-1
- FR-13: Split into FR-13a (description fallback) and FR-13b (note without summary)
- NFR-1: Clarify measurement method — "wall clock time minus Bedrock API call duration" is ambiguous

**Missing artifacts**:
| Artifact | Spec Reference | Status |
|----------|---------------|--------|
| `playlists.yaml` | FR-14, migration script | Present at repo root |
| `tests/fixtures/tool_schemas.json` | CONTRACT-3 | Missing — create in Step 8 |
| Labeled test videos (10 videos) | EVAL-2 | Missing — create in Step 4 |
| `vault/queries/*.md` | FR-10 | Missing — create in Step 10 |

---

## Phase 7 — Exploratory Testing Checklist

| Area | Persona | Heuristic | Time Box |
|------|---------|-----------|----------|
| URL parsing | Developer | Boundary: unusual YouTube URL formats (shorts, embed, mobile) | 15 min |
| Transcript language | Developer | Boundary: video with 10+ available languages | 10 min |
| Vault write | Developer | Interruption: kill process mid-write, check for partial files | 15 min |
| Classification | Developer | Unusual data: video with no description, 1-word title | 10 min |
| Migration | Developer | Concurrency: run two migrate processes simultaneously | 20 min |
| MCP tool | End-user (via Claude Desktop) | Abuse: pass malformed URL, empty string, playlist URL to add_video | 15 min |
| Retry logic | Developer | Interruption: simulate network drop during Bedrock call | 15 min |
| Large playlist | Developer | Boundary: playlist with 200+ videos | 20 min |
| Vault path | Developer | Unusual data: vault path with spaces, unicode characters | 10 min |
| Frontmatter | Developer | Boundary: video title with YAML special characters (`"`, `:`, `#`) | 10 min |
