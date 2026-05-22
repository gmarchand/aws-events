# Research: youtube-transcript-api

## Package Info
- **Package**: `youtube-transcript-api`
- **Source**: https://github.com/jdepoix/youtube-transcript-api
- **Install**: `pip install youtube-transcript-api`

## API Usage

```python
from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()

# Fetch transcript with language priority
transcript = ytt_api.fetch(video_id, languages=['fr', 'en'])

# List available transcripts
transcript_list = ytt_api.list(video_id)

# Transcript object metadata
# transcript.video_id, transcript.language, transcript.language_code
# transcript.is_generated, transcript.is_translatable
```

## Error Handling

Granular exceptions available:
- `TranscriptsDisabled` — subtitles disabled for video
- `NoTranscriptFound` — no transcript in requested languages
- `VideoUnavailable` — video no longer available
- `VideoUnplayable` — video unplayable
- `InvalidVideoId` — bad video ID
- `AgeRestricted` — requires authentication
- `IpBlocked` / `RequestBlocked` — IP blocked by YouTube (need proxies)
- `CouldNotRetrieveTranscript` — base exception for all failures

## Key Considerations for Pipeline

1. **Rate limiting**: No official rate limit, but YouTube may block IPs with heavy usage. Need exponential backoff + potential proxy support.
2. **Language detection**: Can specify language priority list `languages=['fr', 'en']`. Falls back through list.
3. **Auto-generated vs manual**: Can distinguish via `is_generated` flag.
4. **Output format**: Returns list of `{'text': str, 'start': float, 'duration': float}` segments.
5. **No API key needed**: Scrapes YouTube directly (no quota cost).

## Risks
- IP blocking on heavy usage (hundreds of videos)
- Some videos have no subtitles at all
- Auto-generated subtitles may have quality issues
