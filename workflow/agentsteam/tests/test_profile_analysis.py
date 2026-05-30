from schemas.profile_analysis import ProfileAnalysis
from schemas.score_repo import RepoScore, CompletionState
from pydantic import ValidationError
import pytest


def make_repo_score(name="my-repo", score=7):
    return RepoScore(
        name=name,
        score=score,
        has_readme=True,
        completion_state=CompletionState.complete,
        has_license=True,
        has_tests=True,
        last_commit_days_ago=10,
        content_summary="A tool that does X",
        analysis_summary="Clean and well documented",
    )


class TestProfileAnalysis:
    def test_valid_profile(self):
        profile = ProfileAnalysis(
            github_username="flifenstein",
            repos=[make_repo_score()],
            patterns=["mostly ML projects", "no CI pipelines"],
            strengths=["Good READMEs"],
            weaknesses=["Missing tests"],
            overall_analysis="Solid profile with room to grow",
            role="ML Engineer",
            optimizing_for="job applications",
            strongest_repo="inference-bench",
            weakest_repo="old-scraper",
            profile_score=7,
        )
        assert profile.github_username == "flifenstein"
        assert len(profile.repos) == 1

    def test_profile_score_too_high(self):
        with pytest.raises(ValidationError):
            ProfileAnalysis(
                github_username="flifenstein",
                repos=[make_repo_score()],
                patterns=[],
                strengths=["Good"],
                weaknesses=["None"],
                overall_analysis="Great",
                role="Engineer",
                optimizing_for="fun",
                strongest_repo="repo-a",
                weakest_repo="repo-b",
                profile_score=11,
            )

    def test_profile_score_too_low(self):
        with pytest.raises(ValidationError):
            ProfileAnalysis(
                github_username="flifenstein",
                repos=[make_repo_score()],
                patterns=[],
                strengths=["Good"],
                weaknesses=["None"],
                overall_analysis="Great",
                role="Engineer",
                optimizing_for="fun",
                strongest_repo="repo-a",
                weakest_repo="repo-b",
                profile_score=0,
            )

    def test_repos_must_be_list(self):
        with pytest.raises(ValidationError):
            ProfileAnalysis(
                github_username="flifenstein",
                repos="not-a-list",
                patterns=[],
                strengths=["Good"],
                weaknesses=["None"],
                overall_analysis="Great",
                role="Engineer",
                optimizing_for="fun",
                strongest_repo="repo-a",
                weakest_repo="repo-b",
                profile_score=7,
            )
