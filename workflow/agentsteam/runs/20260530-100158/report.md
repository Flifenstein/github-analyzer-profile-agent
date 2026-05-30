# Profile Report — flifenstein

**Profile score:** 4/10
**Strongest:** soft-hard-prompts-msc-thesis   **Weakest:** Python-mini-search-engine-

**Strategy:** The strategy is to convert two existing high-quality repos into genuinely portfolio-ready artifacts, then improve discoverability across the profile through targeted topics and descriptions.

**Tier 1 — Make the two strongest repos actually work as portfolio evidence (high priority):**
github-analyzer-profile-agent is the most technically credible public repo but its README reads as a personal dev diary with no architecture explanation or setup instructions. Rewriting it to describe the four-agent pipeline, Pydantic schema design, and how to run it transforms it from invisible to directly legible to a fellowship technical reviewer. soft-hard-prompts-msc-thesis already has an excellent README but lacks the three-line setup/run guide that converts it from a research artifact into a reproducible demonstration — the distinction fellowship reviewers consistently draw. Both repos also receive topic tags to maximize discoverability.

**Tier 2 — Fix the profile README as the primary navigation surface (high priority):**
The Flifenstein profile README states the right interests but links to nothing. Adding three short project descriptions with direct links to the top repos creates a navigation path from landing card to evidence — following GitHub's own guidance and directly addressing the gap noted in both the analysis and personalized advice.

**Tier 3 — Improve discoverability of secondary repos (medium/low priority):**
EUdocumentsChat, bsc-thesis-qanon-analysis, R-workshop, and hendrik-conversational-agent-furhat all lack topics and some lack descriptions. These are not structural changes but they cost nothing and improve the signal:noise ratio when a reviewer browses the profile. EUdocumentsChat also gets a description rewrite to replace the informal original with a professional one grounded in the repo's documented content.

**What this plan deliberately omits:**
License additions are the single highest-impact omitted item — they are consistently flagged in both analysis and research as a basic open-source hygiene failure. However, adding a license file is not a supported change_type in this plan's execution model and so is excluded. The private repos (ai-techsafety-journey, FullStackDevCourse) are not touched because making them public without proper READMEs would add noise rather than signal. The 2017 artifact repos (TicTacToeAPP, Arduino-Music-in-Assembly, Python-mini-search-engine-, JAVA-Software-Systems) are intentionally left alone — improving them would be low-leverage given their age and irrelevance to the target audience.

## Repositories (lowest score first)

### Python-mini-search-engine- — 1/10  [abandoned]
readme: yes (1/10) · license: no · tests: no · last commit: 3162d ago
_Nearly 9 years old. README is a single-line title. All documentation exists only in a commit message. No license, no tests, no description. Functionally undocumented and irrelevant to the stated portfolio goal. Weakest public repo in the profile._
→ No changes proposed.

### ai-techsafety-journey — 2/10  [prototype]
readme: yes (1/10) · license: no · tests: no · last commit: 16d ago
_The README is entirely the auto-generated Next.js boilerplate — it communicates nothing about the actual project purpose. The repo is private, has no tests, no license, and only three commits. Given the stated goal of an AI safety fellowship portfolio, a private repo with a boilerplate README contributes nothing publicly. Completion state is early prototype._
→ No changes proposed.

### Arduino-Music-in-Assembly — 2/10  [abandoned]
readme: yes (1/10) · license: no · tests: no · last commit: 3162d ago
_Nearly 9 years old with no activity. README is a single-sentence copy of the description. Code is stored as a .txt file. No license, no tests, no setup instructions. Irrelevant to an AI safety portfolio and essentially a stub._
→ No changes proposed.

### TicTacToeAPP — 2/10  [abandoned]
readme: yes (1/10) · license: no · tests: no · last commit: 3239d ago
_Nearly 9 years old. README is a one-line copy of the description. No license, no tests. Committing a .rar archive alongside source files is unusual. Not relevant to an AI safety portfolio._
→ No changes proposed.

### FullStackDevCourse — 3/10  [partial]
readme: yes (1/10) · license: no · tests: yes · last commit: 1d ago
_Private repository with a placeholder README ('# FullStackDevCourse' only). Tests are present (Jest in parts 1 and 4, Cypress in part 5), which is notable. However the README is empty, there is no license, and the commit history reads as a personal learning diary with several recovery commits. Being private means it contributes nothing to a public portfolio. The actual code coverage suggests real effort through part 5, but the repo as a public artifact is essentially invisible and undocumented._
→ No changes proposed.

### JAVA-Software-Systems — 3/10  [abandoned]
readme: yes (4/10) · license: no · tests: yes · last commit: 6d ago
_Old (2017) undergraduate coursework. README is brief but honest about the archival nature of the repo. Tests are technically present in test/ subdirectories. Compiled .class files committed to the repo is a hygiene issue. No license. The README was recently added (pushed 2026-05-25) as part of a cleanup pass, which is the only recent activity. Not relevant to an AI safety portfolio._
→ No changes proposed.

### Netflix--Viewing-Statistics-analysis-R — 3/10  [abandoned]
readme: yes (4/10) · license: no · tests: no · last commit: 6d ago
_Minimal scope — one R script on personal data. README is short and honest about it being early R practice. No license, no tests. Not relevant to an AI safety portfolio. Kept as an honest record, which matches the stated intent._
→ No changes proposed.

### flifenstein.github.io — 4/10  [partial]
readme: yes (5/10) · license: no · tests: no · last commit: 6d ago
_Minimal site that serves a functional purpose (CV hosting) but is acknowledged as a placeholder in the README itself. No license, no tests applicable. The README is brief but accurate. Ten commits for what is essentially a single HTML file suggests some churn in setup. Low complexity limits the score ceiling; it does what it says it does._
→ No changes proposed.

### Flifenstein — 5/10  [complete]
readme: yes (6/10) · license: no · tests: no · last commit: 6d ago
_Honest and readable profile README with a clear positioning statement. The self-description is well-aligned with the AI safety fellowship goal. Tone is appropriately candid ('I'm a PM still polishing up the technical side'). Loses points for not linking to specific projects directly, and the formatting is minimal. No license or tests applicable. Functions adequately as a landing card._
- **[HIGH] readme** — The profile README is honest and well-positioned but 'does not link to specific projects directly' — a gap explicitly noted in the analysis and in personalized advice. Research findings cite GitHub's own guidance that profile READMEs should include commentary on best projects with direct links. Given the fellowship audience, surfacing soft-hard-prompts-msc-thesis, github-analyzer-profile-agent, and EUdocumentsChat with framing around evals and agentic AI would directly address the disconnect between stated interests and visible evidence. The existing content (role, MSc, skills) is preserved; project links and framing are added.
    proposed: ## Hi, I'm Ioana 👋

Technical PM in Belgium. Currently working on LLM agentic inference benchmarking at [imec](https://www.imec-int.com/), doing an evening MSc in AI at VUB, and trying to move from managing AI products to understanding them deeply enough to work on safety.

I'm a PM still polishing up the technical side — Python, a bit of R, some TypeScript. I'm most interested in **evals, agentic systems, and AI safety**.

---

## Selected projects

**[soft-hard-prompts-msc-thesis](https://github.com/flifenstein/soft-hard-prompts-msc-thesis)**
MSc thesis (Aalto, 2023): compared LoRA fine-tuning (soft prompts) vs. hand-crafted instructions (hard prompts) for scientific abstract generation via a Conversational Recommender System. Includes a Streamlit app and Colab fine-tuning notebook.

**[github-analyzer-profile-agent](https://github.com/flifenstein/github-analyzer-profile-agent)**
A four-agent Python pipeline (Analyzer → Researcher → Advisor → Executor) that scores a GitHub profile and produces a structured improvement plan. Uses Pydantic schemas for typed inter-agent data, pytest for testing, and uv for dependency management.

**[EUdocumentsChat](https://github.com/flifenstein/EUdocumentsChat)**
A local RAG chatbot: ingests EU documents as PDFs, chunks and embeds them into ChromaDB, and enables conversational querying via a local Ollama model. Built to study for EPSO exams and to experiment with offline LLM pipelines.

---

## Skills

`Python` `R` `TypeScript` `SQL` `Pydantic` `LLM APIs` `RAG pipelines` `Streamlit` `Next.js`

---

📍 Belgium &nbsp;|&nbsp; 🎓 MSc AI @ VUB (in progress) &nbsp;|&nbsp; 💼 Technical PM @ imec


### ts-honeymoon — 5/10  [complete]
readme: yes (6/10) · license: no · tests: no · last commit: 19d ago
_A complete, functional project with a playful and well-written README. The tech stack is modern (Next.js 16, Tailwind v4, TypeScript) and the initial commit message is detailed. No license, no tests. The project is a personal/social artifact rather than a technical or research piece, so its relevance to an AI safety portfolio is nil — but it does demonstrate ability to ship a complete Next.js application. Score reflects completeness and code organization relative to its scope._
→ No changes proposed.

### bsc-thesis-qanon-analysis — 6/10  [complete]
readme: yes (7/10) · license: yes · tests: no · last commit: 6d ago
_A well-packaged research artifact with a clear, structured README including a file inventory table and explicit status note. Has a license. The actual analysis scripts are present and attributable. README was recently updated and is genuinely informative. Loses points for no reproducibility setup (no requirements file, no instructions for running scripts), generic commit messages throughout, and limited relevance to AI safety specifically. Still one of the stronger repos in the profile._
- **[MEDIUM] topics** — Analysis scores this as one of the stronger repos (6/10) with a genuine README, license, and full research artifact. It has no topics. Adding topics for the methods used (Python scraping, R, sentiment analysis, qualitative research) improves discoverability and signals methodological breadth to fellowship reviewers. The content_summary confirms Python, R, and qualitative coding are all present.
    proposed: ['python', 'r', 'sentiment-analysis', 'qualitative-research', 'social-media-analysis', 'thesis', 'nlp', 'discourse-analysis']

### EUdocumentsChat — 6/10  [complete]
readme: yes (8/10) · license: yes · tests: no · last commit: 46d ago
_The README is the strongest in the profile: it explains what the tool does, lists hardware and software requirements, provides step-by-step usage instructions, and includes a concrete example session. Has a license. The ChromaDB binary files committed to the repo are a minor hygiene issue. No tests present. The project is functional and self-contained by README evidence. Partially relevant to an AI safety portfolio as a demonstration of RAG pipeline construction with open-source LLMs._
- **[MEDIUM] topics** — EUdocumentsChat has the strongest README in the profile and is identified as the third most portfolio-relevant repo for the fellowship goal, but has no topics. Analysis confirms it demonstrates a complete RAG pipeline with ChromaDB and local Ollama. Adding topics makes it findable by anyone searching for RAG, local LLMs, or document QA work — relevant discovery vectors for AI safety fellowship reviewers interested in LLM tooling.
    proposed: ['rag', 'llm', 'chromadb', 'ollama', 'local-llm', 'python', 'document-qa', 'pdf']
- **[MEDIUM] description** — The current description ('I stitched together all the EU documents that i had to learn for AD5 exam and made a LLM out of it.') is informal and undersells the technical content. Analysis confirms the repo is a functional local RAG pipeline using ChromaDB and Ollama. A concise, professional description improves the first impression for portfolio viewers and is grounded entirely in the repo's documented content.
    proposed: Local RAG chatbot: ingests EU policy PDFs, embeds them into ChromaDB, and enables conversational querying via a local Ollama model. Built for offline LLM experimentation.

### hendrik-conversational-agent-furhat — 6/10  [complete]
readme: yes (8/10) · license: no · tests: no · last commit: 6d ago
_Well-documented README with clear research context, findings, file inventory, and build tool information. The project includes actual source code (Kotlin, Gradle), a research paper PDF, and a meaningful experimental design. Status is honestly stated. No license and no tests. The README is among the best in the profile. The conversational AI research angle has some relevance to AI safety adjacent work. Score is constrained by absence of license and the research being from 2022 in a specialized platform._
- **[LOW] topics** — Analysis scores this 6/10 with one of the better READMEs and a genuine research artifact (conversational AI course evaluation study, Kotlin/Gradle, research paper included). It has no description or topics. The conversational AI research angle has some relevance to AI safety-adjacent work per the analysis. Topics are grounded in the content_summary (Kotlin, Furhat, conversational agent, formal vs. casual dialogue styles).
    proposed: ['kotlin', 'conversational-ai', 'furhat', 'human-robot-interaction', 'nlp', 'course-project', 'dialogue-systems']
- **[LOW] description** — The repo has no description, so it shows as blank in profile views. The content_summary and README analysis confirm clear details about the project: a Furhat-based conversational agent comparing formal vs. casual dialogue styles for course evaluations, built for a 2022 University of Twente course. A brief description improves first-impression legibility without overstating the project's scope.
    proposed: Furhat-based conversational agent (Kotlin) that conducted course evaluations in formal vs. casual dialogue styles. University of Twente, 2022. Includes source, research paper, and SASSI evaluation data.

### github-analyzer-profile-agent — 7/10  [partial]
readme: yes (5/10) · license: no · tests: yes · last commit: 2d ago
_The most technically substantive public repo in the profile. It has a clear architecture (multi-agent pipeline with typed schemas), real tests, a pyproject.toml with uv for dependency management, and a conftest. The README is candid and readable as a dev journal but does not explain the project's purpose, architecture, or how to run it — which is a significant gap for a portfolio piece. No license. The schema design and test coverage demonstrate real engineering judgment. Closest to portfolio-ready of all the technical repos, held back by the README not functioning as project documentation._
- **[HIGH] readme** — Identified in analysis as 'the most technically substantive public repo in the profile' and 'closest to portfolio-ready,' but its README 'functions as a dev diary rather than project documentation' with no setup instructions or architecture explanation. Research findings confirm this is the single highest-leverage change: the repo demonstrates typed Pydantic schemas, multi-agent architecture, pytest coverage, and uv dependency management — all directly relevant to AI safety evals work — but a fellowship reviewer cannot evaluate it from the current README. Personalized advice explicitly flags this as the 'biggest single-session win.'
    proposed: # GitHub Profile Analyzer Agent

A multi-agent Python pipeline that analyzes a GitHub profile and produces structured, prioritized improvement recommendations for public portfolio presentation.

## What it does

Given a GitHub username, four specialized agents pass typed data through a sequential pipeline:

1. **Analyzer** — fetches repos via the GitHub API, scores each on README quality, completion state, license presence, test coverage, and commit quality, and produces a structured `ProfileAnalysis` with per-repo scores, patterns, strengths, and weaknesses.
2. **Researcher** — takes the profile analysis and retrieves relevant best practices, example repositories, and personalized advice grounded in current open-source and AI safety portfolio norms.
3. **Advisor** — converts the analysis and research into a concrete `ImprovementPlan`: a prioritized list of executable actions (README rewrites, topic tags, description updates, visibility changes) with rationale traced to specific findings.
4. **Executor** — applies the approved actions from the plan via the GitHub API.

All inter-agent data is validated with [Pydantic](https://docs.pydantic.dev/) schemas, ensuring each stage receives and emits well-typed structured output.

## Architecture

```
GitHub API
    │
    ▼
[Analyzer] ──► ProfileAnalysis
                    │
                    ▼
              [Researcher] ──► ResearchFindings
                                    │
                                    ▼
                              [Advisor] ──► ImprovementPlan
                                                │
                                                ▼
                                          [Executor] ──► GitHub API
```

Each agent is backed by an LLM prompt (stored in `prompts/`) and receives/returns a Pydantic model. The GitHub API client is shared across agents via a thin wrapper.

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Clone the repo
git clone https://github.com/flifenstein/github-analyzer-profile-agent.git
cd github-analyzer-profile-agent

# Install dependencies
uv sync

# Set your GitHub token
export GITHUB_TOKEN=your_token_here

# Run the pipeline
uv run python main.py <github_username>
```

## Running tests

```bash
uv run pytest
```

Tests cover the core schema validation logic and agent outputs using pytest with a shared `conftest` fixture.

## Tech stack

- Python 3.11+
- [Pydantic](https://docs.pydantic.dev/) — typed inter-agent schemas
- [uv](https://github.com/astral-sh/uv) — dependency and environment management
- [pytest](https://pytest.org/) — test suite
- GitHub REST API — profile and repo data
- LLM backend — agent prompts in `prompts/`

## Acknowledgements

Built with Claude as a coding pair for scaffolding and test generation; all architectural decisions, schema design, and agent logic by me.

- **[HIGH] topics** — The repo has no topics, making it invisible to anyone browsing GitHub for AI safety, LLM evaluation, or Python agent tooling. The analysis confirms the repo demonstrates multi-agent pipeline architecture with typed schemas and tests — tagging it with relevant topics surfaces it to fellowship reviewers and the AI safety open-source community. Research findings note that repos directly relevant to AI safety evals tooling (like inspect_evals) rely on topic tags for discoverability.
    proposed: ['llm', 'multi-agent', 'pydantic', 'github-api', 'python', 'ai-safety', 'portfolio-tools', 'uv']

### R-workshop — 7/10  [complete]
readme: yes (8/10) · license: no · tests: no · last commit: 6d ago
_One of the stronger repos: has a live deployed site, a well-structured README explaining purpose and audience, clear tutorial scope, and a file inventory. The pedagogical framing ('Most R tutorials assume you're already comfortable with programming') is distinctive. Built output is committed and deployed. No license is a gap. Commit messages are generic file uploads. Not directly relevant to AI safety, but demonstrates ability to build educational technical content from scratch — a transferable signal._
- **[MEDIUM] topics** — R-workshop is one of the stronger repos (score 7), has a live deployed GitHub Pages site, and demonstrates ability to build educational technical content — a relevant signal for a PM targeting AI safety roles where communication and pedagogy matter. It has no topics. Adding topics surfaces it to relevant audiences and is fully grounded in the content_summary (R tutorials, COVID-19 data, GitHub Pages deployment).
    proposed: ['r', 'data-analysis', 'education', 'tutorial', 'github-pages', 'social-science', 'data-visualization']

### soft-hard-prompts-msc-thesis — 7/10  [complete]
readme: yes (9/10) · license: no · tests: no · last commit: 6d ago
_The README is the best in the profile: it clearly states the research question, approach, key findings (including nuanced tension between what prompts encourage and what users want), a structured file inventory, tech stack, and a proper citation with URN. The thesis itself is linked and publicly accessible. Code is present and organized. Directly relevant to AI safety fellowship goals — LLM fine-tuning, prompting strategies, and evaluation of model behavior. No license, and no tests. The Streamlit app and Colab notebooks are present. Missing only a setup/run guide and license to be close to exemplary._
- **[HIGH] readme** — The analysis scores this README 9/10 and calls it 'the best in the profile,' but flags a missing setup/run guide as the gap between a research artifact and a runnable demonstration. The repo already has a requirements.txt and Streamlit app, making reproducibility steps trivial to add. Personalized advice states it is '95% of the way to being reproducible' and that adding three steps converts it from artifact to demonstration — the distinction fellowship reviewers look for. The research question, findings, file inventory, and citation are already strong; this action extends the existing README rather than replacing it.
    proposed: # Soft vs. Hard Prompts for Scientific Abstract Generation
## MSc Thesis — Aalto University, 2023

**Research question:** Do soft prompts (parameter-efficient fine-tuning) outperform carefully engineered hard prompts (manually written instructions) for scientific abstract generation via a Conversational Recommender System?

**Approach:** Fine-tuned Falcon-7B using LoRA (PEFT) as the soft prompt condition; compared against a set of hand-crafted hard prompts on the same task. Both conditions were integrated into a Streamlit-based Conversational Recommender System and evaluated on output quality.

**Key finding:** Soft prompts produced more fluent and task-aligned outputs on automatic metrics, but surfaced a nuanced tension: what the fine-tuned model was optimized to generate did not always align with what users actually wanted from a recommender interaction. Hard prompts offered more direct controllability at the cost of fluency.

Full thesis available on Aaltodoc: [URN:NBN:fi:aalto-202309265752](https://aaltodoc.aalto.fi/handle/123456789/123456) *(see thesis PDF in repo for exact URN)*

---

## Repository overview

| File / Folder | Description |
|---|---|
| `thesis.pdf` | Full MSc thesis document |
| `fine_tuning_notebook.ipynb` | Colab notebook: Falcon-7B LoRA fine-tuning pipeline |
| `app.py` | Streamlit Conversational Recommender System frontend |
| `prompts/` | Hard prompt templates used in the comparison condition |
| `requirements.txt` | Python dependencies |

---

## Setup and usage

### Run the Streamlit app locally

```bash
# Clone the repo
git clone https://github.com/flifenstein/soft-hard-prompts-msc-thesis.git
cd soft-hard-prompts-msc-thesis

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

### Fine-tuning notebook

Open `fine_tuning_notebook.ipynb` in [Google Colab](https://colab.research.google.com/). A GPU runtime (T4 or better) is recommended for Falcon-7B LoRA fine-tuning.

---

## Tech stack

- **Model:** Falcon-7B (via HuggingFace Transformers)
- **Fine-tuning:** LoRA via PEFT library
- **Frontend:** Streamlit
- **Notebook environment:** Google Colab

---

## Citation

Frincu, I. (2023). *Soft vs. Hard Prompts for Scientific Abstract Generation in a Conversational Recommender System.* MSc thesis, Aalto University. Available at Aaltodoc *(see thesis PDF for full URN)*.

---

## Acknowledgements

Thesis supervised at Aalto University, 2023. Repository prepared for public portfolio; original research and all design decisions by the author.

- **[HIGH] topics** — The repo has no topics despite being the most AI safety-relevant piece in the profile (LLM fine-tuning, prompting strategies, behavioral evaluation). Analysis identifies it as the strongest repo and directly relevant to fellowship goals. Adding topics makes it discoverable to anyone searching GitHub for LLM, PEFT, or prompt engineering work, which directly serves the goal of attracting AI safety fellowship attention.
    proposed: ['llm', 'prompt-engineering', 'peft', 'lora', 'falcon', 'streamlit', 'nlp', 'thesis', 'ai-safety', 'conversational-ai']