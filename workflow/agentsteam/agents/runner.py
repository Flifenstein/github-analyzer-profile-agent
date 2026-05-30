import anthropic
from typing import TypeVar, Type
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

_client = anthropic.Anthropic()


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
    text = "".join(b.text for b in response.content if b.type == "text")
    return schema.model_validate_json(_strip_fences(text))


def _strip_fences(text: str) -> str:
    """Models sometimes wrap JSON in ```json ... ``` fences despite instructions."""
    text = text.strip()
    if text.startswith("```"):
        # drop the opening fence line (``` or ```json) and the closing fence
        text = text.split("\n", 1)[1] if "\n" in text else text
        if text.endswith("```"):
            text = text[: -len("```")]
    return text.strip()
