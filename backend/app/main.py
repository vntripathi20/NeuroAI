"""FastAPI application entry point.

Run locally with:
    uvicorn app.main:app --reload --port 8000
(from the backend/ directory, with the project virtual environment active)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import health
from app.core.config import settings

app = FastAPI(
    title="NeuroAI Backend",
    description="API for the NeuroAI speech-based neurological screening research project.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "NeuroAI backend is running."}
