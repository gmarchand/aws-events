# PDD Summary: youtube-to-vault

## Project Overview

Refactoring of the `aws-events` repository into a **MCP Server** (`youtube-to-vault`) that transforms YouTube videos and playlists into structured Obsidian vault notes with AI-generated summaries via Amazon Bedrock Claude Opus 4.

## Artifacts Created

| File | Purpose |
|------|---------|
| `rough-idea.md` | Initial concept and context |
| `idea-honing.md` | 19 Q&A requirements clarification |
| `research/youtube-transcript-api.md` | API usage, errors, limitations |
| `research/bedrock-converse-api.md` | Converse API pattern, pricing, retry |
| `research/obsidian-vault-patterns.md` | Frontmatter, Dataview, MOC patterns |
| `research/youtube-data-api.md` | Quota system, API usage |
| `design/detailed-design.md` | Full architecture, components, interfaces, data models |
| `design/test-plan-annex.md` | EARS requirements, 5-layer test pyramid, LLM-eval rubrics |
| `implementation/plan.md` | 10-step incremental implementation plan |
| `implementation/test-requirements.md` | ~55 acceptance criteria mapped by step |

## Architecture Summary

```
MCP Clients (Claude Desktop, Kiro, Migration Script)
        │
        ▼
FastMCP Server (stdio)
        │
        ▼
Core Library
├── youtube.py      → YouTube Data API v3
├── transcript.py   → youtube-transcript-api
├── classifier.py   → Bedrock Claude Opus 4
├── summarizer.py   → Bedrock Claude Opus 4
├── vault.py        → Obsidian vault filesystem
└── pipeline.py     → Orchestrator
        │
        ▼
Obsidian Vault (thematic/year/playlist/notes)
```

## Key Design Decisions

1. **MCP Server** (not CLI) — enables daily use from any AI assistant
2. **FastMCP + stdio** — simplest deployment, no server management
3. **Core library shared** — MCP Server and migration script use same code
4. **Bedrock Claude Opus 4** — maximum summary quality
5. **youtube-transcript-api** — free, no API key needed
6. **Vault structure**: `thematic/year/playlist/notes` — browsable hierarchy
7. **Idempotent + retry/backoff** — safe to re-run, resilient to transient errors

## Cost Estimate

~$189 for 500 videos (dominated by Opus 4 summarization at ~$0.375/video).

## Next Steps

1. **Generate code tasks** from the implementation plan using `@code-task-generator`
2. **Delegate implementation** to `coder` agent, step by step
3. **Run tests** after each step (TDD cycle)
4. **Migration** — run the migration script against real playlists.yaml once all steps pass

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| IP blocking by YouTube on heavy transcript fetch | Exponential backoff, pauses between requests |
| Bedrock throttling on batch processing | Adaptive retry (boto3 built-in), rate limiting |
| LLM classification accuracy | Confidence threshold, candidates returned for human review |
| Cost overrun on large batches | Dry-run mode, per-video cost logging |
