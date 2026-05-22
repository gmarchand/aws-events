"""Tests for classifier.py — AC-4.1 through AC-4.7."""
from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest
from botocore.exceptions import ClientError

from youtube_to_vault.core.classifier import classify_video, detect_clients
from youtube_to_vault.core.youtube import VideoMetadata


@pytest.fixture
def metadata():
    return VideoMetadata(
        video_id="ABC123",
        title="AWS Media Day 2023",
        description="TF1 and Canal+ discuss live streaming on AWS.",
        published_at="2023-07-27T10:00:00Z",
        channel_title="AWS France",
        language="fr",
        playlist_id=None,
        playlist_title=None,
    )


def _mock_converse_response(text: str) -> dict:
    return {"output": {"message": {"content": [{"text": text}]}}}


def _throttling_error():
    return ClientError(
        {"Error": {"Code": "ThrottlingException", "Message": "Rate exceeded"}},
        "Converse",
    )


@patch("youtube_to_vault.core.classifier.boto3.client")
def test_classify_known_thematic(mock_boto, metadata):
    """AC-4.1: Known thematic returned when confidence high."""
    payload = {"thematic": "media", "confidence": 0.95, "candidates": [], "is_media_client": True}
    mock_client = MagicMock()
    mock_client.converse.return_value = _mock_converse_response(json.dumps(payload))
    mock_boto.return_value = mock_client

    result = classify_video(metadata, ["media", "ai"])

    assert result.thematic == "media"
    assert result.confidence == 0.95
    assert result.is_media_client is True


@patch("youtube_to_vault.core.classifier.boto3.client")
def test_classify_low_confidence(mock_boto, metadata):
    """AC-4.2: Low confidence returns candidates, thematic=None."""
    payload = {"thematic": None, "confidence": 0.4, "candidates": ["media", "ai"], "is_media_client": False}
    mock_client = MagicMock()
    mock_client.converse.return_value = _mock_converse_response(json.dumps(payload))
    mock_boto.return_value = mock_client

    result = classify_video(metadata, ["media", "ai"])

    assert result.thematic is None
    assert result.candidates == ["media", "ai"]


@patch("youtube_to_vault.core.classifier.boto3.client")
def test_classify_malformed_json(mock_boto, metadata):
    """AC-4.3: Malformed JSON handled gracefully."""
    mock_client = MagicMock()
    mock_client.converse.return_value = _mock_converse_response("not valid json at all")
    mock_boto.return_value = mock_client

    result = classify_video(metadata, [])

    assert result.thematic is None
    # No exception raised


@patch("youtube_to_vault.core.classifier.boto3.client")
def test_classify_throttling_retry(mock_boto, metadata):
    """AC-4.4: ThrottlingException triggers retry."""
    payload = {"thematic": "media", "confidence": 0.9, "candidates": [], "is_media_client": True}
    mock_client = MagicMock()
    mock_client.converse.side_effect = [
        _throttling_error(),
        _throttling_error(),
        _mock_converse_response(json.dumps(payload)),
    ]
    mock_boto.return_value = mock_client

    result = classify_video(metadata, [])

    assert result.thematic == "media"
    assert mock_client.converse.call_count == 3


@patch("youtube_to_vault.core.classifier.boto3.client")
def test_classify_only_title_description_sent(mock_boto, metadata):
    """AC-4.5: Only title and description sent to Bedrock (not transcript)."""
    payload = {"thematic": "media", "confidence": 0.9, "candidates": [], "is_media_client": True}
    mock_client = MagicMock()
    mock_client.converse.return_value = _mock_converse_response(json.dumps(payload))
    mock_boto.return_value = mock_client

    classify_video(metadata, [])

    call_kwargs = mock_client.converse.call_args
    messages = call_kwargs[1]["messages"] if call_kwargs[1] else call_kwargs[0][1]
    user_text = messages[0]["content"][0]["text"]
    assert metadata.title in user_text
    assert metadata.description[:100] in user_text
    # classify_video signature doesn't accept transcript — it's not a parameter


@patch("youtube_to_vault.core.classifier.boto3.client")
def test_detect_clients_returns_list(mock_boto, metadata):
    """AC-4.6: Client detection returns list of names."""
    mock_client = MagicMock()
    mock_client.converse.return_value = _mock_converse_response('["TF1", "Canal+"]')
    mock_boto.return_value = mock_client

    result = detect_clients(metadata, "TF1 and Canal+ were present.")

    assert result == ["TF1", "Canal+"]


@patch("youtube_to_vault.core.classifier.boto3.client")
def test_classify_confidence_clamped(mock_boto, metadata):
    """AC-4.7: Confidence is always in [0.0, 1.0]."""
    # Test with out-of-range values
    for raw_confidence, expected in [(1.5, 1.0), (-0.3, 0.0), (0.8, 0.8)]:
        payload = {"thematic": "media", "confidence": raw_confidence, "candidates": [], "is_media_client": False}
        mock_client = MagicMock()
        mock_client.converse.return_value = _mock_converse_response(json.dumps(payload))
        mock_boto.return_value = mock_client

        result = classify_video(metadata, [])
        assert 0.0 <= result.confidence <= 1.0, f"confidence {result.confidence} out of range for input {raw_confidence}"
