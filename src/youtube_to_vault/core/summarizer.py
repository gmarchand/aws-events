from __future__ import annotations

import os

import boto3
from botocore.exceptions import ClientError
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential

from youtube_to_vault.core.youtube import VideoMetadata

_MODEL_ID = "us.anthropic.claude-opus-4-7"

_SYSTEM_PROMPT = """\
You are an expert technical writer specializing in AWS and cloud computing content.
Summarize the provided video content following these strict rules:

1. STYLE: Active voice, full sentences, flowing paragraphs organized by theme. No filler phrases.
   Formal yet engaging tone. Narrative prose — NO bullet points, NO numbered lists.
2. FORMAT: Use exactly 3 levels of Markdown headings (# ## ###). Write well-developed paragraphs
   with logical flow. The summary must be fully understandable without watching the video.
3. FOCUS: Key decisions, action items, important discussions, and outcomes. Concise and clear.

Write the summary in the language specified in the user message.\
"""


def _is_throttling(exc: BaseException) -> bool:
    return isinstance(exc, ClientError) and exc.response["Error"]["Code"] == "ThrottlingException"


def _bedrock_client():
    region = os.environ.get("AWS_REGION", "us-east-1")
    return boto3.client("bedrock-runtime", region_name=region)


@retry(
    retry=retry_if_exception(_is_throttling),
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=1, max=30),
    reraise=True,
)
def generate_summary(
    transcript: str | None,
    description: str,
    metadata: VideoMetadata,
    language: str,
) -> str:
    """Generate a structured markdown summary via Bedrock Claude Opus 4."""
    client = _bedrock_client()

    if transcript:
        content_section = f"Transcript:\n{transcript}"
    else:
        content_section = f"Description (no transcript available):\n{description}"

    user_msg = (
        f"Write the summary in language: {language}\n\n"
        f"Video title: {metadata.title}\n\n"
        f"{content_section}"
    )

    response = client.converse(
        modelId=_MODEL_ID,
        system=[{"text": _SYSTEM_PROMPT}],
        messages=[{"role": "user", "content": [{"text": user_msg}]}],
        inferenceConfig={"maxTokens": 4096},
    )
    return response["output"]["message"]["content"][0]["text"]
