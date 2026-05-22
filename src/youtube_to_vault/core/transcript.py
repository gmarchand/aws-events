from __future__ import annotations

from dataclasses import dataclass

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from youtube_transcript_api import (
    IpBlocked,
    NoTranscriptFound,
    RequestBlocked,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
    YouTubeTranscriptApiException,
)


@dataclass
class TranscriptResult:
    text: str = ""
    language: str = ""
    is_generated: bool = False
    available: bool = False


_FALLBACK_LANGUAGES = ["fr", "en"]


@retry(
    retry=retry_if_exception_type((IpBlocked, RequestBlocked)),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    reraise=True,
)
def _fetch_with_retry(video_id: str, languages: list[str]) -> TranscriptResult:
    """Inner fetch — retried on IpBlocked/RequestBlocked."""
    api = YouTubeTranscriptApi()
    transcript_list = api.list(video_id)
    transcript = transcript_list.find_transcript(languages)
    fetched = transcript.fetch()
    text = " ".join(s.text for s in fetched)
    return TranscriptResult(
        text=text,
        language=transcript.language_code,
        is_generated=transcript.is_generated,
        available=True,
    )


def fetch_transcript(
    video_id: str,
    preferred_languages: list[str] | None = None,
) -> TranscriptResult:
    """Fetch transcript for a video. Returns TranscriptResult(available=False) on any failure."""
    languages = list(preferred_languages) if preferred_languages else []
    # Append fallbacks if not already present
    for lang in _FALLBACK_LANGUAGES:
        if lang not in languages:
            languages.append(lang)

    try:
        return _fetch_with_retry(video_id, languages)
    except (IpBlocked, RequestBlocked):
        # Exhausted retries
        return TranscriptResult()
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable):
        return TranscriptResult()
    except YouTubeTranscriptApiException:
        return TranscriptResult()
    except Exception:  # noqa: BLE001
        return TranscriptResult()
