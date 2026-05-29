from pydantic import BaseModel


#easy to verify where the source is from
class Source(BaseModel):
    title: str
    url: str

class ResearchFindings(BaseModel):
    best_practices: list[str]
    example_repos: list[str] 
    personalized_advice: list[str]
    sources : list[Source]
    search_queries_used: list[str]

