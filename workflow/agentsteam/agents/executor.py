import base64
import requests
from tools.github_client import GitHubWriter
from schemas.improvement_plan import ImprovementPlan, ImprovementAction, ChangeType
from schemas.improvement_action import ApprovedChanges, RejectedAction, ExecutionResult


def _apply_action(action: ImprovementAction, writer: GitHubWriter) -> tuple[bool, str | None]:
    try:
        if action.change_type == ChangeType.description:
            writer.update_description(action.repo_name, action.new_content)
        elif action.change_type == ChangeType.topics:
            writer.update_topics(action.repo_name, action.new_topics)
        elif action.change_type == ChangeType.visibility:
            writer.update_visibility(action.repo_name, action.new_content)
        elif action.change_type == ChangeType.readme:
            writer.update_readme(action.repo_name, action.new_content)
        return True, None
    except requests.HTTPError as e:
        return False, str(e)


def run_executor(
    plan: ImprovementPlan,
    approved_indices: set[int],
    writer: GitHubWriter,
) -> ApprovedChanges:
    rejected = []
    results = []

    for i, action in enumerate(plan.actions):
        if i not in approved_indices:
            rejected.append(RejectedAction(action=action, reason="Not explicitly approved by user"))
        else:
            succeeded, error = _apply_action(action, writer)
            results.append(ExecutionResult(action=action, succeeded=succeeded, error_message=error))

    return ApprovedChanges(
        github_username=plan.github_username,
        rejected=rejected,
        results=results,
    )
