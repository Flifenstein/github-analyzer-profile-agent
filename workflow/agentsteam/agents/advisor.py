import json
import anthropic
from schemas.improvement_plan import ImprovementPlan

client = anthropic.Anthropic()


def run_advisor(
    profile_analysis_json: str,
    research_findings_json: str,
    system_prompt: str,
) -> ImprovementPlan:
    combined = json.dumps({
        "profile_analysis": json.loads(profile_analysis_json),
        "research_findings": json.loads(research_findings_json),
    })
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": combined}],
    )
    text = "".join(b.text for b in response.content if b.type == "text")
    data = json.loads(text)
    return ImprovementPlan(**data)
