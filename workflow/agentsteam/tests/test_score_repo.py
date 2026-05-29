from schemas.score_repo import RepoScore, CompletionState
from pydantic import ValidationError
import pytest


def make_repo_score(**kwargs):
    defaults = dict(
        name="Name-repo",
        score=8,
        has_readme=True,
        completion_state=CompletionState.complete,
        has_license=True,
        has_tests=True,
        last_commit_days_ago=10,
        content_summary="A tool that does X",
        analysis_summary="Clean and well documented",
    )
    defaults.update(kwargs)
    return RepoScore(**defaults)


class TestRepoScore:
    def test_valid_score(self):
        score = make_repo_score()
        assert score.name == "Name-repo"
        assert score.score == 8
        assert score.has_readme is True

    def test_invalid_name(self):
        with pytest.raises(ValidationError):
            make_repo_score(name=9)

    def test_invalid_score_outofbound(self):
        with pytest.raises(ValidationError):
            make_repo_score(score=11)

    def test_invalid_score_invalid(self):
        with pytest.raises(ValidationError):
            make_repo_score(score="high")

    def test_invalid_score_negative(self):
        with pytest.raises(ValidationError):
            make_repo_score(score=-1)

    def test_invalid_has_readme(self):
        with pytest.raises(ValidationError):
            make_repo_score(has_readme="maybe")
