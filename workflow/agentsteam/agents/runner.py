import json
import anthropic
from typing import TypeVar, Type
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

# Entry-tier orgs get 30k input tokens/min. The three agents run back-to-back,
# so a later call can hit the per-minute cap. The SDK honors the 429 retry-after
# header — give it enough attempts to wait out the window instead of crashing.
_client = anthropic.Anthropic(max_retries=6)


def run_agent(
    system_prompt: str,
    user_content: str,
    schema: Type[T],
    *,
    web_search: bool = False,
    max_tokens: int = 4096,
) -> T:
    kwargs: dict = dict(
        model="claude-sonnet-4-6",
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )
    if web_search:
        kwargs["tools"] = [{"type": "web_search_20250305", "name": "web_search"}]

    response = _client.messages.create(**kwargs)
    if response.stop_reason == "max_tokens":
        raise ValueError(
            f"{schema.__name__} response was cut off at max_tokens={max_tokens} "
            f"(the JSON is incomplete). Increase max_tokens for this agent."
        )
    text = "".join(b.text for b in response.content if b.type == "text")
    return schema.model_validate(_extract_json(text))


def _extract_json(text: str) -> dict | list:
    """Pull the JSON object/array out of a model response.

    Handles the common ways a model wraps its JSON despite instructions:
    leading prose ("Now I have enough to..."), ```json fences, and trailing
    commentary. We locate the first { or [ and decode exactly one JSON value
    from there, ignoring anything before or after it.
    """
    candidates = [i for i in (text.find("{"), text.find("[")) if i != -1]
    if not candidates:
        raise ValueError(f"No JSON object found in model response: {text[:200]!r}")
    start = min(candidates)
    # raw_decode stops at the end of the first complete value, so trailing
    # fences or prose after the JSON are simply ignored.
    obj, _ = json.JSONDecoder().raw_decode(text[start:])
    return obj
