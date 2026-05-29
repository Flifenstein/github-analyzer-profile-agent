from pydantic import BaseModel, model_validator
from enum import Enum


# only the fields that Agent 4 can actually act on via the GitHub API
class ChangeType(str, Enum):
    description = "description"  
    topics = "topics"            
    readme = "readme"            
    visibility = "visibility"     

class Priority(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class ImprovementAction(BaseModel):
    repo_name: str
    change_type: ChangeType
    priority: Priority
    rationale: str               
    new_content: str | None = None       # for description, readme, visibility, etc
    new_topics: list[str] | None = None  # only used when change_type == topics
    @model_validator(mode="after")
    def check_content(self):
        if self.change_type == ChangeType.topics and not self.new_topics:
            raise ValueError("new_topics must be provided when change_type is topics")
        if self.change_type != ChangeType.topics and not self.new_content:
            raise ValueError("new_content must be provided when change_type is not topics")
        return self


class ImprovementPlan(BaseModel):
    github_username: str
    actions: list[ImprovementAction]
    summary_plan: str

