import json
import anthropic
from schemas.profile_analysis import ProfileAnalysis

client = anthropic.Anthropic()


def run_analyzer(github_data_json: str, system_prompt: str) -> ProfileAnalysis:
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=8096,
        system=system_prompt,
        messages=[{"role": "user", "content": github_data_json}],
    )
    text = "".join(b.text for b in response.content if b.type == "text")
    data = json.loads(text)
    return ProfileAnalysis(**data)
