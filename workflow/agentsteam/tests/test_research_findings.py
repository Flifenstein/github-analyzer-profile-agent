from schemas.research_findings import ResearchFindings, Source
from pydantic import ValidationError
import pytest


class TestSource:
    def test_valid_source(self):
        source = Source(title="GitHub Docs", url="https://docs.github.com")
        assert source.title == "GitHub Docs"
        assert source.url == "https://docs.github.com"

    def test_missing_title(self):
        with pytest.raises(ValidationError):
            Source(url="https://docs.github.com")

    def test_missing_url(self):
        with pytest.raises(ValidationError):
            Source(title="GitHub Docs")


class TestResearchFindings:
    def test_valid_findings(self):
        findings = ResearchFindings(
            best_practices=["add a license", "write a README"],
            example_repos=["torvalds/linux"],
            personalized_advice=["add tests to inference-bench"],
            sources=[Source(title="GitHub Docs", url="https://docs.github.com")],
            search_queries_used=["github best practices 2024"],
        )
        assert len(findings.best_practices) == 2
        assert len(findings.sources) == 1

    def test_empty_lists_are_valid(self):
        findings = ResearchFindings(
            best_practices=[],
            example_repos=[],
            personalized_advice=[],
            sources=[],
            search_queries_used=[],
        )
        assert findings.best_practices == []

    def test_invalid_best_practices_not_a_list(self):
        with pytest.raises(ValidationError):
            ResearchFindings(
                best_practices="add a license",
                example_repos=[],
                personalized_advice=[],
                sources=[],
                search_queries_used=[],
            )

    def test_missing_required_field(self):
        with pytest.raises(ValidationError):
            ResearchFindings(
                best_practices=["add a license"],
                example_repos=[],
                personalized_advice=[],
                sources=[],
            )
