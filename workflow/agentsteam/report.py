"""Render a ProfileAnalysis + ImprovementPlan into a readable per-repo report.

Usable two ways:
  - imported by pipeline.py to print/save a report at the end of a run
  - run standalone against a saved run folder:
        python report.py runs/20260530-143022
"""
import sys
from collections import defaultdict
from pathlib import Path

from schemas.profile_analysis import ProfileAnalysis
from schemas.improvement_plan import ImprovementPlan


def _flags(repo) -> str:
    readme = f"yes ({repo.readme_quality}/10)" if repo.has_readme else "no"
    return (
        f"readme: {readme} · license: {'yes' if repo.has_license else 'no'} · "
        f"tests: {'yes' if repo.has_tests else 'no'} · "
        f"last commit: {repo.last_commit_days_ago}d ago"
    )


def build_report(profile: ProfileAnalysis, plan: ImprovementPlan) -> str:
    # group proposed actions by repo name
    actions_by_repo: dict[str, list] = defaultdict(list)
    for action in plan.actions:
        actions_by_repo[action.repo_name].append(action)

    lines: list[str] = []
    lines.append(f"# Profile Report — {profile.github_username}")
    lines.append("")
    lines.append(f"**Profile score:** {profile.profile_score}/10")
    lines.append(f"**Strongest:** {profile.strongest_repo}   "
                 f"**Weakest:** {profile.weakest_repo}")
    lines.append("")
    lines.append(f"**Strategy:** {plan.summary_plan}")
    lines.append("")
    lines.append("## Repositories (lowest score first)")

    # worst-scoring repos first — those need the most attention
    for repo in sorted(profile.repos, key=lambda r: r.score):
        lines.append("")
        lines.append(f"### {repo.name} — {repo.score}/10  [{repo.completion_state.value}]")
        lines.append(_flags(repo))
        lines.append(f"_{repo.analysis_summary}_")

        actions = actions_by_repo.get(repo.name, [])
        if not actions:
            lines.append("→ No changes proposed.")
            continue

        # high-priority actions first
        order = {"high": 0, "medium": 1, "low": 2}
        for a in sorted(actions, key=lambda x: order[x.priority.value]):
            detail = a.new_topics if a.change_type.value == "topics" else a.new_content
            lines.append(
                f"- **[{a.priority.value.upper()}] {a.change_type.value}** — {a.rationale}"
            )
            lines.append(f"    proposed: {detail}")

    return "\n".join(lines)


def _load_run(run_dir: Path) -> tuple[ProfileAnalysis, ImprovementPlan]:
    profile = ProfileAnalysis.model_validate_json(
        (run_dir / "2_profile_analysis.json").read_text()
    )
    plan = ImprovementPlan.model_validate_json(
        (run_dir / "4_improvement_plan.json").read_text()
    )
    return profile, plan


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python report.py <run_folder>   e.g. python report.py runs/20260530-143022")
    run_dir = Path(sys.argv[1])
    profile, plan = _load_run(run_dir)
    report = build_report(profile, plan)
    print(report)
    out = run_dir / "report.md"
    out.write_text(report)
    print(f"\nSaved → {out}")
