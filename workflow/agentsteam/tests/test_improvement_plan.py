from schemas.improvement_plan import (
    ImprovementAction,
    ImprovementPlan,
    ChangeType,
    Priority,
)
from pydantic import ValidationError
import pytest


def make_action(change_type=ChangeType.readme, **kwargs):
    defaults = dict(
        repo_name="inference-bench",
        change_type=change_type,
        priority=Priority.high,
        rationale="Missing documentation",
        new_content="# inference-bench\nA benchmarking tool." if change_type != ChangeType.topics else None,
        new_topics=["machine-learning", "benchmarking"] if change_type == ChangeType.topics else None,
    )
    defaults.update(kwargs)
    return ImprovementAction(**defaults)


class TestImprovementAction:
    def test_valid_readme_action(self):
        action = make_action(change_type=ChangeType.readme)
        assert action.change_type == ChangeType.readme
        assert action.new_content is not None
        assert action.new_topics is None

    def test_valid_topics_action(self):
        action = make_action(change_type=ChangeType.topics)
        assert action.change_type == ChangeType.topics
        assert action.new_topics == ["machine-learning", "benchmarking"]

    def test_valid_description_action(self):
        action = make_action(change_type=ChangeType.description, new_content="A fast benchmarking tool")
        assert action.new_content == "A fast benchmarking tool"

    def test_valid_visibility_action(self):
        action = make_action(change_type=ChangeType.visibility, new_content="public")
        assert action.new_content == "public"

    def test_topics_without_new_topics_raises(self):
        with pytest.raises(ValidationError):
            ImprovementAction(
                repo_name="inference-bench",
                change_type=ChangeType.topics,
                priority=Priority.high,
                rationale="Add tags",
                new_topics=None,
            )

    def test_readme_without_new_content_raises(self):
        with pytest.raises(ValidationError):
            ImprovementAction(
                repo_name="inference-bench",
                change_type=ChangeType.readme,
                priority=Priority.high,
                rationale="Write a README",
                new_content=None,
            )

    def test_invalid_change_type(self):
        with pytest.raises(ValidationError):
            ImprovementAction(
                repo_name="inference-bench",
                change_type="delete_everything",
                priority=Priority.high,
                rationale="Some reason",
                new_content="something",
            )

    def test_invalid_priority(self):
        with pytest.raises(ValidationError):
            ImprovementAction(
                repo_name="inference-bench",
                change_type=ChangeType.readme,
                priority="urgent",
                rationale="Some reason",
                new_content="something",
            )


class TestImprovementPlan:
    def test_valid_plan(self):
        plan = ImprovementPlan(
            github_username="flifenstein",
            actions=[make_action()],
            summary_plan="Focus on documentation first",
        )
        assert plan.github_username == "flifenstein"
        assert len(plan.actions) == 1

    def test_empty_actions_is_valid(self):
        plan = ImprovementPlan(
            github_username="flifenstein",
            actions=[],
            summary_plan="Nothing to do",
        )
        assert plan.actions == []
