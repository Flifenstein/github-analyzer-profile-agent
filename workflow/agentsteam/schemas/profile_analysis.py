#this is easy cuz is just all the repo scores and then a few guidance on the profile itself + plus me (role, optimizing_for) and examples like weakest and strongets repo

from pydantic import BaseModel, Field
from schemas.score_repo import RepoScore

class ProfileAnalysis(BaseModel):
    github_username: str
    repos : list[RepoScore]
    patterns : list[str]
    strengths : list[str]
    weaknesses : list[str]
    overall_analysis : str
    role : str
    optimizing_for: str
    strongest_repo : str
    weakest_repo : str
    profile_score : int = Field(ge=1, le=10)
