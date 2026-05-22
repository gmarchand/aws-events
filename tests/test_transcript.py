"""Tests for transcript.py — AC-3.1 through AC-3.7."""
from unittest.mock import MagicMock

from youtube_transcript_api import (
    IpBlocked,
    NoTranscriptFound,
    TranscriptsDisabled,
)
from youtube_transcript_api._transcripts import FetchedTranscript, FetchedTranscriptSnippet

from youtube_to_vault.core.transcript import fetch_transcript


def _make_fetched(snippets_text: list[str], language_code: str = "en", is_generated: bool = False):
    snippets = [FetchedTranscriptSnippet(text=t, start=float(i), duration=1.0) for i, t in enumerate(snippets_text)]
    return FetchedTranscript(
        snippets=snippets,
        video_id="test",
        language="English",
        language_code=language_code,
        is_generated=is_generated,
    )


def _make_transcript_mock(language_code: str, is_generated: bool, fetched: FetchedTranscript):
    t = MagicMock()
    t.language_code = language_code
    t.is_generated = is_generated
    t.fetch.return_value = fetched
    return t


def _patch_api(mocker, list_side_effect=None, find_side_effect=None, find_return=None):
    """Patch YouTubeTranscriptApi() instance."""
    mock_api = MagicMock()
    mock_list = MagicMock()

    if list_side_effect:
        mock_api.list.side_effect = list_side_effect
    else:
        mock_api.list.return_value = mock_list

    if find_side_effect:
        mock_list.find_transcript.side_effect = find_side_effect
    elif find_return:
        mock_list.find_transcript.return_value = find_return

    mocker.patch("youtube_to_vault.core.transcript.YouTubeTranscriptApi", return_value=mock_api)
    return mock_api, mock_list


# ---------------------------------------------------------------------------
# AC-3.1 — Preferred language selected when available
# ---------------------------------------------------------------------------

def test_preferred_language_selected(mocker):
    fetched = _make_fetched(["Bonjour"], language_code="fr")
    transcript_mock = _make_transcript_mock("fr", False, fetched)
    _patch_api(mocker, find_return=transcript_mock)

    result = fetch_transcript("VID", ["fr", "en"])

    assert result.available is True
    assert result.language == "fr"


# ---------------------------------------------------------------------------
# AC-3.2 — Fallback to available language when preferred absent
# ---------------------------------------------------------------------------

def test_fallback_language(mocker):
    fetched = _make_fetched(["Hello"], language_code="en")
    transcript_mock = _make_transcript_mock("en", False, fetched)

    mock_api, mock_list = _patch_api(mocker)
    # find_transcript called with ["fr", "en"] — returns "en" transcript
    mock_list.find_transcript.return_value = transcript_mock

    result = fetch_transcript("VID", ["fr"])

    assert result.available is True
    assert result.language == "en"
    # Verify find_transcript was called with fr first, then en as fallback
    call_args = mock_list.find_transcript.call_args[0][0]
    assert "fr" in call_args
    assert "en" in call_args


# ---------------------------------------------------------------------------
# AC-3.3 — TranscriptsDisabled returns unavailable result
# ---------------------------------------------------------------------------

def test_transcripts_disabled(mocker):
    _patch_api(mocker, list_side_effect=TranscriptsDisabled("VID"))

    result = fetch_transcript("VID")

    assert result.available is False
    assert result.text == ""


# ---------------------------------------------------------------------------
# AC-3.4 — NoTranscriptFound returns unavailable result
# ---------------------------------------------------------------------------

def test_no_transcript_found(mocker):
    mock_api, mock_list = _patch_api(mocker)
    mock_list.find_transcript.side_effect = NoTranscriptFound("VID", ["fr", "en"], mock_list)

    result = fetch_transcript("VID")

    assert result.available is False


# ---------------------------------------------------------------------------
# AC-3.5 — IpBlocked retries with backoff then returns unavailable
# ---------------------------------------------------------------------------

def test_ip_blocked_exhausts_retries(mocker):
    # Patch tenacity to not actually wait
    mocker.patch("youtube_to_vault.core.transcript.wait_exponential", return_value=MagicMock(return_value=0))

    call_count = 0

    def raise_ip_blocked(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        raise IpBlocked("VID")

    mock_api = MagicMock()
    mock_api.list.side_effect = raise_ip_blocked
    mocker.patch("youtube_to_vault.core.transcript.YouTubeTranscriptApi", return_value=mock_api)

    result = fetch_transcript("VID")

    assert result.available is False
    assert call_count == 3  # max 3 attempts


# ---------------------------------------------------------------------------
# AC-3.6 — IpBlocked succeeds on retry
# ---------------------------------------------------------------------------

def test_ip_blocked_succeeds_on_retry(mocker):
    mocker.patch("youtube_to_vault.core.transcript.wait_exponential", return_value=MagicMock(return_value=0))

    fetched = _make_fetched(["Hello world"], language_code="en")
    transcript_mock = _make_transcript_mock("en", False, fetched)

    call_count = 0

    def list_side_effect(video_id):
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise IpBlocked(video_id)
        mock_list = MagicMock()
        mock_list.find_transcript.return_value = transcript_mock
        return mock_list

    mock_api = MagicMock()
    mock_api.list.side_effect = list_side_effect
    mocker.patch("youtube_to_vault.core.transcript.YouTubeTranscriptApi", return_value=mock_api)

    result = fetch_transcript("VID")

    assert result.available is True
    assert result.text == "Hello world"
    assert call_count == 3


# ---------------------------------------------------------------------------
# AC-3.7 — Segments concatenated into single text
# ---------------------------------------------------------------------------

def test_segments_concatenated(mocker):
    fetched = _make_fetched(["Hello", "world"], language_code="en")
    transcript_mock = _make_transcript_mock("en", False, fetched)
    _patch_api(mocker, find_return=transcript_mock)

    result = fetch_transcript("VID")

    assert result.text == "Hello world"
    assert result.available is True
