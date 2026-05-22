from schemas.score_repo import RepoScore
from pydantic import ValidationError
import pytest


class TestRepoScore:
    def test_valid_score(self):
        score = RepoScore(name="Name-repo", score=8, has_readme=True)
        assert score.name == "Name-repo"
        assert score.score == 8
        assert score.has_readme is True

    def test_invalid_name(self):
        with pytest.raises(ValidationError):
            RepoScore(name=9, score=8, has_readme=True)

    def test_invalid_score_outofbound(self):
        with pytest.raises(ValidationError):
            RepoScore(name="Name-repo", score=11, has_readme=True)

    def test_invalid_score_invalid(self):
        with pytest.raises(ValidationError):
            RepoScore(name="Name-repo", score="high", has_readme=True)

    def test_invalid_score_negative(self):
        with pytest.raises(ValidationError):
            RepoScore(name="Name-repo", score=-1, has_readme=True)

    def test_invalid_has_readme(self):
        with pytest.raises(ValidationError):
            RepoScore(name="Name-repo", score=8, has_readme="maybe")
