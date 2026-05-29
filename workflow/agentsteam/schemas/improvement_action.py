from pydantic import BaseModel
from schemas.improvement_plan import ImprovementAction


class RejectedAction(BaseModel):
    action: ImprovementAction
    reason: str


class ExecutionResult(BaseModel):
    action: ImprovementAction
    succeeded: bool
    error_message: str | None = None


class ApprovedChanges(BaseModel):
    github_username: str
    rejected: list[RejectedAction]
    results: list[ExecutionResult]
