"""Tests for summarizer.py — AC-5.1 through AC-5.5."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from botocore.exceptions import ClientError

from youtube_to_vault.core.summarizer import generate_summary
from youtube_to_vault.core.youtube import VideoMetadata


@pytest.fixture
def metadata():
    return VideoMetadata(
        video_id="ABC123",
        title="AWS Media Day 2023",
        description="Prime Video presents its live streaming architecture.",
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


@patch("youtube_to_vault.core.summarizer.boto3.client")
def test_summary_returned(mock_boto, metadata):
    """AC-5.1: Summary returned from mocked Bedrock."""
    expected = "# Summary\n\nThis is the summary."
    mock_client = MagicMock()
    mock_client.converse.return_value = _mock_converse_response(expected)
    mock_boto.return_value = mock_client

    result = generate_summary("transcript text", metadata.description, metadata, "fr")

    assert result == expected


@patch("youtube_to_vault.core.summarizer.boto3.client")
def test_description_only_no_transcript_in_prompt(mock_boto, metadata):
    """AC-5.2: Description-only path omits transcript from prompt."""
    mock_client = MagicMock()
    mock_client.converse.return_value = _mock_converse_response("summary")
    mock_boto.return_value = mock_client

    generate_summary(None, metadata.description, metadata, "en")

    call_kwargs = mock_client.converse.call_args[1]
    user_text = call_kwargs["messages"][0]["content"][0]["text"]
    assert "Transcript:" not in user_text
    assert "Description" in user_text


@patch("youtube_to_vault.core.summarizer.boto3.client")
def test_language_instruction_in_prompt(mock_boto, metadata):
    """AC-5.3: Language instruction included in prompt."""
    mock_client = MagicMock()
    mock_client.converse.return_value = _mock_converse_response("summary")
    mock_boto.return_value = mock_client

    generate_summary("transcript", metadata.description, metadata, "fr")

    call_kwargs = mock_client.converse.call_args[1]
    user_text = call_kwargs["messages"][0]["content"][0]["text"]
    assert "fr" in user_text


@patch("youtube_to_vault.core.summarizer.boto3.client")
def test_bedrock_called_with_correct_params(mock_boto, metadata):
    """AC-5.4: Bedrock called with maxTokens=4096, temperature=0.3."""
    mock_client = MagicMock()
    mock_client.converse.return_value = _mock_converse_response("summary")
    mock_boto.return_value = mock_client

    generate_summary("transcript", metadata.description, metadata, "fr")

    call_kwargs = mock_client.converse.call_args[1]
    inference = call_kwargs["inferenceConfig"]
    assert inference["maxTokens"] == 4096
    assert inference["temperature"] == pytest.approx(0.3)


@patch("youtube_to_vault.core.summarizer.boto3.client")
def test_throttling_retry(mock_boto, metadata):
    """AC-5.5: ThrottlingException triggers retry."""
    mock_client = MagicMock()
    mock_client.converse.side_effect = [
        _throttling_error(),
        _throttling_error(),
        _mock_converse_response("summary after retry"),
    ]
    mock_boto.return_value = mock_client

    result = generate_summary("transcript", metadata.description, metadata, "fr")

    assert result == "summary after retry"
    assert mock_client.converse.call_count == 3
