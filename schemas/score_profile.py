# score should be bteween 1 and 10, with 10 being top notch developers repo level that is creative, clean, easy to fork. 
# 2 is a incomplete repo with, bad readme.md, not reproducible, bad messy code
#my aim is to score somewhere on btw 7-8

from pydantic import BaseModel, Field

class ScoreProfile(BaseModel):
    name: str
    score: int = Field (ge=1, le=10)
    hasreadme: bool


