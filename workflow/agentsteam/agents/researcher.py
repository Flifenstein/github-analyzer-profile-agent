import json
import anthropic
from schemas.research_findings import ResearchFindings

client = anthropic.Anthropic()

def run_researcher(profile_analysis_json, system_prompt) -> ResearchFindings:
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": profile_analysis_json}],
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
    )

    text = "".join(b.text for b in response.content if b.type == "text")
    data = json.loads(text)
    return ResearchFindings(**data)