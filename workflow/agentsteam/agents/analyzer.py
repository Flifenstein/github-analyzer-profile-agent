from agents.runner import run_agent
from schemas.profile_analysis import ProfileAnalysis


def run_analyzer(github_data_json: str, system_prompt: str) -> ProfileAnalysis:
    return run_agent(system_prompt, github_data_json, ProfileAnalysis, max_tokens=8096)
