# GitHub Profile Analyzer Agent

A multi-agent Python pipeline that analyzes a GitHub profile and produces a
structured, prioritized plan for improving how those repos read as a public
portfolio. It scores every repo, researches current best practices with web
search, and emits a concrete list of changes (README rewrites, topic tags,
description updates) — each one traced back to a specific finding.

I built it to clean up my own neglected repos and target them at AI safety
research fellowship applications, but the role and goal are configurable.

## What it does

Given a GitHub username, the pipeline passes typed data through three LLM
agents and renders a report:

1. **Analyzer** — pulls every repo via the GitHub REST API (README, file tree,
   recent commits, topics, visibility) and scores each one on README quality,
   completion state, license, tests, and commit quality. Emits a typed
   `ProfileAnalysis` with per-repo scores, profile-wide patterns, strengths,
   and weaknesses.
2. **Researcher** — takes the analysis and uses Claude's web search to ground
   itself in current open-source and portfolio norms, producing
   `ResearchFindings` with best practices and personalized advice.
3. **Advisor** — combines analysis + research into an `ImprovementPlan`: a
   prioritized list of executable actions, each with a rationale tied to a
   specific finding.

A fourth component, the **Executor**, can apply approved actions back to GitHub
via the API (description / topics / visibility / README writes). It exists and
is tested, but is **not yet wired into the automated pipeline** — by design, so
nothing writes to your account without an explicit approval step. See
[Status & honesty notes](#status--honesty-notes).

Every inter-agent boundary is a [Pydantic](https://docs.pydantic.dev/) schema,
so each stage receives and emits validated, well-typed structured output.

## Architecture

```
GitHub REST API
      │  repos, READMEs, file trees, commits
      ▼
 [Analyzer] ──► ProfileAnalysis
                     │
                     ▼
               [Researcher] ──► ResearchFindings        (+ web search)
                     │
                     ▼
                [Advisor] ──► ImprovementPlan
                     │
                     ▼
                [report.py] ──► report.md  +  numbered JSON traces

 ImprovementPlan ──► [Executor] ──► GitHub REST API   (separate, opt-in)
```

Each agent is a thin wrapper around a shared `run_agent` helper
(`agents/runner.py`) that calls the Claude API, enforces a JSON contract, and
validates the result against the agent's Pydantic schema. Prompts live as plain
text in `prompts/`; the GitHub client (`tools/github_client.py`) is split into a
read-only `GitHubReader` and a write-side `GitHubWriter`.

### Layout

```
workflow/agentsteam/
├── pipeline.py            # orchestrator + entry point
├── config.py              # loads + validates env vars
├── report.py              # renders ProfileAnalysis + ImprovementPlan → report.md
├── agents/
│   ├── runner.py          # shared Claude call + JSON extraction + schema validation
│   ├── analyzer.py
│   ├── researcher.py
│   ├── advisor.py
│   └── executor.py        # opt-in write-back (not in the auto pipeline)
├── prompts/               # one .txt system prompt per agent
├── schemas/               # Pydantic contracts between stages
├── tools/github_client.py # GitHubReader / GitHubWriter
├── tests/                 # pytest suite (schema + scoring logic)
└── runs/                  # timestamped run traces (gitignored, except one example)
```

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency
management and targets Python 3.13+.

```bash
git clone https://github.com/flifenstein/github-analyzer-profile-agent.git
cd github-analyzer-profile-agent

# Install dependencies (incl. dev group for tests)
uv sync
```

Create a `.env` (see `infoenv/.env.example`) with:

```env
ANTHROPIC_API_KEY=sk-ant-...
GITHUB_TOKEN=ghp_...          # a token with repo read scope is enough for analysis
GITHUB_USERNAME=your-github-username
```

Then edit the two lines at the top of `workflow/agentsteam/pipeline.py` to match
who you are and what you're optimizing the profile for:

```python
ROLE = "technical product manager"
OPTIMIZING_FOR = "clean, well-documented public portfolio targeted towards AI safety research fellowships"
```

## Running it

The pipeline runs from inside the `workflow/agentsteam/` directory (imports are
relative to it):

```bash
cd workflow/agentsteam
uv run python pipeline.py
```

This creates `runs/<timestamp>/` containing numbered JSON traces for each stage
plus a final `report.md`.

### Resuming a run

Agent calls cost tokens, so completed stages are cached to disk. Re-running a
folder reuses any finished steps (profile analysis, research) instead of paying
for them again:

```bash
uv run python pipeline.py runs/20260530-100158
```

You can also re-render a report from a saved run without calling any agents:

```bash
uv run python report.py runs/20260530-100158
```

### Example output

A complete real run is committed as an example:
[`workflow/agentsteam/runs/20260530-100158/`](workflow/agentsteam/runs/20260530-100158/)
— the four stage JSONs plus the rendered
[`report.md`](workflow/agentsteam/runs/20260530-100158/report.md). All other run
folders are gitignored.

## Running tests

```bash
uv run pytest
```

Tests cover the Pydantic schema validation and the repo/profile scoring logic,
using a shared `conftest.py` fixture.

## Tech stack

- **Python 3.13+**
- **[Pydantic](https://docs.pydantic.dev/)** — typed inter-agent schemas
- **[Anthropic SDK](https://github.com/anthropics/anthropic-sdk-python)** — Claude (`claude-sonnet-4-6`) + web search tool
- **[uv](https://github.com/astral-sh/uv)** — dependency and environment management
- **[pytest](https://pytest.org/)** — test suite
- **[ruff](https://github.com/astral-sh/ruff)** — linting / naming conventions
- **GitHub REST API** — profile and repo data (and opt-in write-back)

## How it was built

This was a deliberate "do it properly this time" project, built over a few days:

- Scaffolded the structure, then wrote the repo-scoring logic first.
- Committed to `uv` for dependency management from the start.
- Adopted Pydantic for the data schemas (an LLM suggestion early on that turned
  out to be the right backbone for the whole agent-to-agent contract idea).
- Wrote a real pytest suite, and added ruff after one too many `snake_case`
  slips.
- Designed the agent contracts on paper first:
  `Analyzer → ProfileAnalysis`, `Researcher → ResearchFindings`,
  `Advisor → ImprovementPlan`. The improvement plan was the hardest to reason
  through — it needed a custom validator for proposed topic changes.

## Status & honesty notes

This is a working but unfinished project, and I want to be straight about how it
came together:

- The first three stages run end-to-end and produce the committed example report.
- The **Executor** (write-back to GitHub) is implemented and tested but
  intentionally not yet hooked into the pipeline — I want a human-in-the-loop
  approval step before anything edits a real account.
- **Disclosure:** I leaned on Claude heavily for the last stretch — getting the
  three-agent **orchestrator (`pipeline.py`) running** and **fixing the JSON
  parsing bugs** in `agents/runner.py` (models wrapping their JSON in prose and
  code fences). I'd almost given up at that point and used a lot of AI help to
  push it over the line. I plan to go back and redo those parts myself so I
  fully own them; everything else — the architecture, schema design, scoring
  logic, and agent prompts — is my own work.
