# score should be bteween 1 and 10, with 10 being top notch developers repo level that is creative, clean, easy to fork.
# 2 is a incomplete repo with, bad readme.md, not reproducible, bad messy code
# my aim is to score somewhere on btw 7-8 per repo
# realized i should add a profile score separatley and rename this ScoreProfile to socreRepo
# lots of back anf forth on the data schema, but this should be enough context for the Agent 1 to tell to Agent 2
# key elements are the content and anlysis summary but all the others are helpful data for me to make sure the score is justified

from pydantic import BaseModel, Field
from enum import Enum

#completion state of the repo, subjective to the agent
class CompletionState(str, Enum):
    prototype = "prototype"
    partial = "partial"
    complete = "complete"
    abandoned = "abandoned"

class RepoScore(BaseModel):
    name: str
    score: int = Field(ge=1, le=10)
    has_readme: bool
    description: str | None = None #really optional
    readme_quality: int | None =  Field(default=None, ge=1, le=10)
    completion_state :  CompletionState
    has_license : bool
    has_tests : bool
    last_commit_days_ago : int
    commit_quality : str | None
    content_summary : str #what the repo does
    analysis_summary: str # Agent 1 's opinion

