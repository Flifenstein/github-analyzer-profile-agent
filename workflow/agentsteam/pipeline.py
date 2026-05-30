import base64
import json
from datetime import datetime
from pathlib import Path

import config
from tools.github_client import GitHubReader
from agents.analyzer import run_analyzer
from agents.researcher import run_researcher
from agents.advisor import run_advisor

PROMPTS_DIR = Path(__file__).parent / "prompts"
RUNS_DIR = Path(__file__).parent / "runs"

# Edit these to match who you are and what you're optimizing for
ROLE = "technical product manager"
OPTIMIZING_FOR = "clean, well-documented public portfolio targeted towards AI safety research fellowships"


def _load_prompt(name: str) -> str:
    return (PROMPTS_DIR / f"{name}.txt").read_text()


def _decode_readme(raw: dict | None) -> str | None:
    if raw is None:
        return None
    content = raw.get("content", "")
    return base64.b64decode(content).decode("utf-8")


def gather_repo_data(reader: GitHubReader) -> str:
    repos_raw = reader.list_repos()
    repos = []
    for r in repos_raw:
        name = r["name"]
        readme_raw = reader.get_readme(name)
        try:
            file_tree = reader.get_file_tree(name)
        except Exception:
            file_tree = []
        try:
            commits = reader.get_commits(name)
        except Exception:
            commits = []

        repos.append({
            "name": name,
            "description": r.get("description"),
            "topics": r.get("topics", []),
            "visibility": r.get("visibility"),
            "pushed_at": r.get("pushed_at"),
            "has_readme": readme_raw is not None,
            "readme_content": _decode_readme(readme_raw),
            "file_tree": file_tree,
            "recent_commits": commits,
        })

    return json.dumps({
        "github_username": config.GITHUB_USERNAME.strip(),
        "role": ROLE,
        "optimizing_for": OPTIMIZING_FOR,
        "repos": repos,
    })


def _trace(run_dir: Path, step: str, payload_json: str) -> None:
    """Print a short banner to the terminal and dump the full JSON to a file."""
    print(f"\n{'=' * 60}\n[{step}]\n{'=' * 60}")
    print(payload_json)
    (run_dir / f"{step}.json").write_text(payload_json)


def run_pipeline():
    run_dir = RUNS_DIR / datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=True)
    print(f"Run traces → {run_dir}")

    reader = GitHubReader(config.GITHUB_TOKEN, config.GITHUB_USERNAME.strip())
    raw_data = gather_repo_data(reader)
    _trace(run_dir, "1_github_data", json.dumps(json.loads(raw_data), indent=2))

    profile = run_analyzer(raw_data, _load_prompt("analyzer"))
    profile_json = profile.model_dump_json()
    _trace(run_dir, "2_profile_analysis", profile.model_dump_json(indent=2))

    research = run_researcher(profile_json, _load_prompt("researcher"))
    research_json = research.model_dump_json()
    _trace(run_dir, "3_research_findings", research.model_dump_json(indent=2))

    plan = run_advisor(profile_json, research_json, _load_prompt("advisor"))
    _trace(run_dir, "4_improvement_plan", plan.model_dump_json(indent=2))

    print(f"\nDone. All traces saved under {run_dir}")


if __name__ == "__main__":
    run_pipeline()
