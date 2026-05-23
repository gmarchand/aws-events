from __future__ import annotations

import json
import os
from dataclasses import dataclass, field

import boto3
from botocore.exceptions import ClientError
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential

from youtube_to_vault.core.youtube import VideoMetadata

_MODEL_ID = "us.anthropic.claude-opus-4-7"


def _is_throttling(exc: BaseException) -> bool:
    return isinstance(exc, ClientError) and exc.response["Error"]["Code"] == "ThrottlingException"


def _bedrock_client():
    region = os.environ.get("AWS_REGION", "us-east-1")
    return boto3.client("bedrock-runtime", region_name=region)


@dataclass
class ClassificationResult:
    thematic: str | None
    confidence: float
    candidates: list[str] = field(default_factory=list)
    is_media_client: bool = False


@retry(
    retry=retry_if_exception(_is_throttling),
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=1, max=30),
    reraise=True,
)
def _converse(client, messages: list[dict], system: str) -> str:
    response = client.converse(
        modelId=_MODEL_ID,
        system=[{"text": system}],
        messages=messages,
        inferenceConfig={"maxTokens": 512},
    )
    return response["output"]["message"]["content"][0]["text"]


def classify_video(
    metadata: VideoMetadata, existing_thematics: list[str]
) -> ClassificationResult:
    """Classify a video by thematic using title+description only (cost-aware)."""
    client = _bedrock_client()
    thematics_hint = (
        f"Known thematics: {existing_thematics}. Prefer one of these if it fits."
        if existing_thematics
        else "No existing thematics yet — suggest a new one."
    )
    system = (
        "You are a video classifier. Respond ONLY with valid JSON, no markdown fences.\n"
        "Output schema: {\"thematic\": string|null, \"confidence\": float, "
        "\"candidates\": list[string], \"is_media_client\": bool}\n"
        f"{thematics_hint}\n"
        "Set thematic=null and populate candidates if confidence < 0.7."
    )
    user_msg = f"Title: {metadata.title}\n\nDescription: {metadata.description[:1000]}"
    try:
        raw = _converse(client, [{"role": "user", "content": [{"text": user_msg}]}], system)
        data = json.loads(raw)
        confidence = float(data.get("confidence", 0.0))
        confidence = max(0.0, min(1.0, confidence))
        return ClassificationResult(
            thematic=data.get("thematic"),
            confidence=confidence,
            candidates=data.get("candidates", []),
            is_media_client=bool(data.get("is_media_client", False)),
        )
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        return ClassificationResult(thematic=None, confidence=0.0)


def detect_clients(metadata: VideoMetadata, transcript: str | None) -> list[str]:
    """Extract client/company names from video content."""
    client = _bedrock_client()
    system = (
        "You are an entity extractor. Extract company and client names mentioned in the content. "
        "Respond ONLY with a JSON array of strings, e.g. [\"TF1\", \"Canal+\"]. "
        "Return [] if none found."
    )
    content = f"Title: {metadata.title}\n\nDescription: {metadata.description[:500]}"
    if transcript:
        content += f"\n\nTranscript excerpt: {transcript[:2000]}"
    try:
        raw = _converse(client, [{"role": "user", "content": [{"text": content}]}], system)
        result = json.loads(raw)
        if isinstance(result, list):
            return [str(x) for x in result]
        return []
    except (json.JSONDecodeError, TypeError):
        return []


def detect_tags(metadata: VideoMetadata, transcript: str | None) -> list[str]:
    """Extract topic tags from video content."""
    client = _bedrock_client()
    system = (
        "You are a topic tagger for media/tech videos. Extract 3-7 relevant topic tags. "
        "Tags should be lowercase, single words or short hyphenated phrases. "
        "Examples: streaming, live, sports, ott, broadcast, ai, cloud-migration, encoding. "
        "Respond ONLY with a JSON array of strings."
    )
    content = f"Title: {metadata.title}\n\nDescription: {metadata.description[:300]}"
    if transcript:
        content += f"\n\nTranscript excerpt: {transcript[:1000]}"
    try:
        raw = _converse(client, [{"role": "user", "content": [{"text": content}]}], system)
        result = json.loads(raw)
        if isinstance(result, list):
            return [str(x).lower() for x in result][:7]
        return []
    except (json.JSONDecodeError, TypeError):
        return []
