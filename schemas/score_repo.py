# score should be bteween 1 and 10, with 10 being top notch developers repo level that is creative, clean, easy to fork.
# 2 is a incomplete repo with, bad readme.md, not reproducible, bad messy code
# my aim is to score somewhere on btw 7-8 per repo
# realized i should add a profile score separatley and rename this ScoreProfile to socreRepo

from pydantic import BaseModel, Field


class RepoScore(BaseModel):
    name: str
    score: int = Field(ge=1, le=10)
    has_readme: bool
