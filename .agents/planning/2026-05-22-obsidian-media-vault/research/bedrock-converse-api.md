# Research: Amazon Bedrock Converse API

## Model ID
- Claude Opus 4: `anthropic.claude-opus-4-20250514-v1:0` (verify availability in region)
- Recommended region: `us-east-1` (broadest model availability)

## Converse API (Recommended over InvokeModel)

```python
import boto3
from botocore.exceptions import ClientError

brt = boto3.client("bedrock-runtime", region_name="us-east-1")

response = brt.converse(
    modelId="anthropic.claude-opus-4-20250514-v1:0",
    messages=[
        {
            "role": "user",
            "content": [{"text": prompt}],
        }
    ],
    system=[{"text": system_prompt}],
    inferenceConfig={"maxTokens": 4096, "temperature": 0.3},
)

response_text = response["output"]["message"]["content"][0]["text"]
```

## Key Design Decisions

1. **Converse vs InvokeModel**: Use Converse — unified API across models, simpler, supports system prompts natively.
2. **System prompt**: Define summarization rules (voice active, paragraphs, 3 heading levels, formal tone) as system prompt.
3. **Token limits**: Claude Opus 4 has 200K context window. A 1h transcript ≈ 15K tokens input. Output max 4096 tokens for summary.
4. **Temperature**: Low (0.2-0.3) for factual summarization.

## Throttling & Retry

- Bedrock returns `ThrottlingException` when rate limited
- Use exponential backoff with jitter
- Default quotas vary by model and region (RPM/TPM)
- boto3 has built-in retry config:

```python
from botocore.config import Config

config = Config(
    retries={"max_attempts": 5, "mode": "adaptive"}
)
brt = boto3.client("bedrock-runtime", config=config)
```

## Cost Estimate (Claude Opus 4)
- Input: ~$15/M tokens
- Output: ~$75/M tokens
- Per video (15K input + 2K output): ~$0.375
- 500 videos: ~$187

## Classification Cost (title+description only)
- ~200 tokens input per video, ~50 tokens output
- 1000 videos classification: ~$0.07 (negligible)

## References
- https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api-ex-python.html
- https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html
