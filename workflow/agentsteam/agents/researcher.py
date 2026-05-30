from agents.runner import run_agent
from schemas.research_findings import ResearchFindings


def run_researcher(profile_analysis_json: str, system_prompt: str) -> ResearchFindings:
    return run_agent(system_prompt, profile_analysis_json, ResearchFindings, web_search=True)
