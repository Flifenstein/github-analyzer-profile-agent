

from schemas.score_profile import ScoreProfile
from pydantic import ValidationError
import pytest


class TestScoreProfile:
    def test_valid_score(self):
        score = ScoreProfile(name="Name-repo", score=8, hasreadme=True)
        assert score.name == "Name-repo"
        assert score.score == 8
        assert score.hasreadme is True

    def test_invalid_name(self):
        with pytest.raises(ValidationError):
            ScoreProfile(name=9, score=11, hasreadme=True)

    def test_invalid_score_outofbound(self):
        with pytest.raises(ValidationError):
            ScoreProfile(name="Name-repo", score=11, hasreadme=True)
    def test_invalid_score_invalid(self):
        with pytest.raises(ValidationError):
            ScoreProfile(name="Name-repo", score="high", hasreadme=True)
    def test_invalid_score_negative(self):
        with pytest.raises(ValidationError):
            ScoreProfile(name="Name-repo", score=-1, hasreadme=True)
    
    def test_invalid_hasreadme(self):
        with pytest.raises(ValidationError):
            ScoreProfile(name="Name-repo", score=8, hasreadme="maybe")
