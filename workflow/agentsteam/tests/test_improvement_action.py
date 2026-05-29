from schemas.improvement_action import (
    RejectedAction,
    ExecutionResult,
    ApprovedChanges,
)
from schemas.improvement_plan import ImprovementAction, ChangeType, Priority
from pydantic import ValidationError
import pytest


def make_action():
    return ImprovementAction(
        repo_name="inference-bench",
        change_type=ChangeType.readme,
        priority=Priority.high,
        rationale="Missing README",
        new_content="# inference-bench\nA benchmarking tool.",
    )


class TestRejectedAction:
    def test_valid_rejected_action(self):
        rejected = RejectedAction(
            action=make_action(),
            reason="README already exists and is detailed enough",
        )
        assert rejected.reason == "README already exists and is detailed enough"
        assert rejected.action.repo_name == "inference-bench"

    def test_missing_reason(self):
        with pytest.raises(ValidationError):
            RejectedAction(action=make_action())


class TestExecutionResult:
    def test_successful_result(self):
        result = ExecutionResult(action=make_action(), succeeded=True)
        assert result.succeeded is True
        assert result.error_message is None

    def test_failed_result_with_error(self):
        result = ExecutionResult(
            action=make_action(),
            succeeded=False,
            error_message="GitHub API rate limit exceeded",
        )
        assert result.succeeded is False
        assert result.error_message == "GitHub API rate limit exceeded"

    def test_missing_succeeded(self):
        with pytest.raises(ValidationError):
            ExecutionResult(action=make_action())


class TestApprovedChanges:
    def test_valid_approved_changes(self):
        approved = ApprovedChanges(
            github_username="flifenstein",
            rejected=[RejectedAction(action=make_action(), reason="Already done")],
            results=[ExecutionResult(action=make_action(), succeeded=True)],
        )
        assert approved.github_username == "flifenstein"
        assert len(approved.rejected) == 1
        assert len(approved.results) == 1

    def test_empty_lists_are_valid(self):
        approved = ApprovedChanges(
            github_username="flifenstein",
            rejected=[],
            results=[],
        )
        assert approved.rejected == []
        assert approved.results == []
