# Research: YouTube Data API v3

## Quota System
- **Daily quota**: 10,000 units per project (default)
- **PlaylistItems.list**: 1 unit per request (50 items max per page)
- **Videos.list**: 1 unit per request (50 videos max per page)
- **Search.list**: 100 units per request (expensive, avoid)

## Cost Calculation for This Project

For a playlist of 50 videos:
- 1 PlaylistItems.list call = 1 unit (gets 50 items)
- 1 Videos.list call per batch of 50 = 1 unit (gets snippet with description)

For ~100 playlists averaging 20 videos each:
- ~100 PlaylistItems.list calls = 100 units
- ~40 Videos.list calls (batched by 50) = 40 units
- **Total: ~140 units** — well within 10,000 daily quota

## API Usage Pattern

```python
from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=GOOGLE_API_KEY)

# Get playlist items
response = youtube.playlistItems().list(
    part='snippet',
    playlistId=playlist_id,
    maxResults=50,
    pageToken=next_page_token
).execute()

# Get video details (batch by ID)
response = youtube.videos().list(
    part='snippet',
    id=','.join(video_ids)  # up to 50 IDs
).execute()
```

## Key Fields from Video Snippet
- `title`: Video title
- `description`: Full description
- `publishedAt`: Publication date
- `channelTitle`: Channel name
- `defaultAudioLanguage`: Language of the video (when available)
- `tags`: Video tags (when available)

## Considerations
- `defaultAudioLanguage` not always set — may need to infer from transcript language
- `description` can be empty or very short for some videos
- Pagination needed for playlists > 50 items
- Single video IDs (not playlist) in playlists.yaml need Videos.list directly

## References
- https://developers.google.com/youtube/v3/getting-started (quota)
- https://developers.google.com/youtube/v3/docs/playlistItems/list
- https://developers.google.com/youtube/v3/docs/videos/list
