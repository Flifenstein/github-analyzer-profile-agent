import json
from agents.runner import run_agent
from schemas.improvement_plan import ImprovementPlan


def run_advisor(
    profile_analysis_json: str,
    research_findings_json: str,
    system_prompt: str,
) -> ImprovementPlan:
    combined = json.dumps({
        "profile_analysis": json.loads(profile_analysis_json),
        "research_findings": json.loads(research_findings_json),
    })
    # The plan can contain full README rewrites for several repos, so it needs
    # a large output budget or the JSON gets truncated mid-string.
    return run_agent(system_prompt, combined, ImprovementPlan, max_tokens=16000)
