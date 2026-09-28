# NeuroAI
NeuroAI is a student research project investigating whether measurable
characteristics of human speech — both **acoustic** (pitch, jitter,
shimmer, MFCCs, speech rate, pauses, spectral features, etc.) and
**linguistic** (vocabulary diversity, sentence structure, repetition,
lexical and semantic characteristics) — correlate with patterns associated
with neurological conditions such as Parkinson's disease and cognitive
impairment.

The research plan is to build and compare three model families
(acoustic-only, linguistic-only, and multimodal acoustic+linguistic) and
use explainable AI methods to study which features drive their
predictions.

## Current status: initial scaffold

**No research has been conducted yet.** This repository currently contains
only project infrastructure:

- A repository structure with placeholders for every stage of the research
  pipeline (see "Repository structure" below).
- A minimal FastAPI backend with a single health-check endpoint.
- A minimal Next.js frontend with a single page that verifies it can reach
  the backend.
- A Python dependency setup and an automated test for the backend.

There is **no data**, **no trained models**, **no extracted features**,
and **no results**. Nothing in this repository should be read as a
scientific finding. Statements about what specific features or models will
be used are stated as *plans*, not conclusions.

## Repository structure

```
NeuroAI/
├── backend/            FastAPI application (app/main.py is the entry point)
├── frontend/            Next.js + TypeScript app
├── data/                raw/, processed/, external/ speech data (gitignored, empty)
├── preprocessing/       audio/text cleaning steps (not yet implemented)
├── feature_extraction/
│   ├── acoustic/        pitch, jitter, shimmer, MFCCs, etc. (not yet implemented)
│   └── linguistic/      vocabulary, syntax, semantics, etc. (not yet implemented)
├── models/
│   ├── acoustic_only/
│   ├── linguistic_only/
│   └── multimodal/      three model families to be compared (not yet implemented)
├── evaluation/          metrics & cross-model comparison (not yet implemented)
├── explainability/      SHAP / feature-importance analysis (not yet implemented)
├── experiments/         experiment configs & driver scripts (not yet implemented)
├── notebooks/           exploratory notebooks (none yet)
├── results/             experiment outputs (gitignored, empty)
├── tests/               automated tests (backend/ tests exist; more to come)
├── paper/               written report/manuscript (not started)
├── requirements.txt      shared Python runtime dependencies
├── requirements-dev.txt  + testing/linting tools
└── pyproject.toml        pytest/ruff/black/mypy configuration
```

Each placeholder folder contains a short README stating what will live
there and, where relevant, why no code exists yet.

## Architectural decisions

- **One Python environment for backend + research code.** The FastAPI
  backend will eventually *use* the preprocessing, feature extraction, and
  model code in this repo (e.g. to run inference on an uploaded clip), so
  they share one virtual environment and one `requirements.txt` rather than
  maintaining two separate dependency sets that would need to stay in sync.
- **Minimal current dependencies.** `requirements.txt` only lists what the
  backend skeleton actually imports (FastAPI, Uvicorn, Pydantic). Heavier,
  domain-specific libraries (`librosa`, `parselmouth`, `spaCy`,
  `scikit-learn`, `torch`, `shap`, ...) will be added when the module that
  needs them is actually implemented, so the dependency list always
  reflects real usage.
- **FastAPI for the backend.** Async-friendly, has automatic OpenAPI docs
  (useful once real inference endpoints exist), and integrates cleanly with
  the Python ML/data ecosystem this project depends on.
- **Next.js + TypeScript for the frontend.** App Router + TypeScript is the
  current standard for a maintainable React frontend; Tailwind is included
  for styling but no real UI has been designed yet — the current page only
  proves connectivity to the backend.
- **CORS configured via environment variable.** The backend reads allowed
  origins from `NEUROAI_CORS_ORIGINS` (see `.env.example`) rather than
  hardcoding `localhost:3000`, so deployment origins can be added later
  without code changes.
- **`data/` and `results/` are gitignored (except their README/.gitkeep).**
  Speech datasets, especially ones involving human subjects, typically
  carry licensing/consent restrictions and should never be committed.
  Experiment results are treated as regenerable outputs of code + data,
  not source-controlled artifacts.
- **Single top-level `tests/` folder.** Keeps all automated tests
  discoverable from one `pytest` invocation at the repo root; backend API
  tests live in `tests/backend/`, and tests for future preprocessing/
  feature-extraction/model code will live alongside them in their own
  subfolders.

## Prerequisites

- Python 3.11+
- Node.js 20+ and npm

## Backend setup (FastAPI)

From the repository root:

```powershell
# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1        # PowerShell
# or: .venv\Scripts\activate.bat  # cmd.exe
# or: source .venv/Scripts/activate  # Git Bash

# Install dependencies (use requirements.txt alone for a leaner runtime-only install)
pip install -r requirements-dev.txt

# Configure environment
copy .env.example .env

# Run the API (from the repo root, pointing uvicorn at the backend app)
uvicorn app.main:app --reload --port 8000 --app-dir backend
```

The API will be available at http://localhost:8000, with interactive docs
at http://localhost:8000/docs. Verify it's running:

```bash
curl http://localhost:8000/health
# {"status":"ok","service":"neuroai-backend"}
```

## Frontend setup (Next.js)

From `frontend/`:

```bash
npm install
copy .env.local.example .env.local   # PowerShell/cmd; use `cp` on macOS/Linux/Git Bash
npm run dev
```

Open http://localhost:3000 — the page reports whether it successfully
reached the backend's `/health` endpoint. Both servers must be running for
the "Connected" status to appear.

## Running tests

From the repository root, with the virtual environment active:

```bash
pytest
```

This currently runs the backend's two smoke tests (`tests/backend/`),
confirming the API starts and its health endpoint responds correctly.

## Next logical development step

With connectivity and project structure established, the next step is
**not** modeling — it's building the first real pipeline stage:

1. Choose (but do not yet download) a candidate public dataset for initial
   development, and document its access/licensing terms in `data/README.md`.
2. Implement basic audio preprocessing (`preprocessing/`): loading,
   resampling, silence trimming.
3. Implement a first, well-justified acoustic feature (e.g. pitch via
   `librosa` or `parselmouth`) in `feature_extraction/acoustic/`, with a
   unit test in `tests/` using a short synthetic or public-domain audio
   clip — before adding any more features or touching modeling.

This keeps each step verifiable in isolation rather than building the full
pipeline speculatively.
