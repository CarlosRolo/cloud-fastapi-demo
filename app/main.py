from fastapi import FastAPI

from app.routers import health, items

app = FastAPI(
    title="Cloud FastAPI Demo",
    description="Containerized FastAPI app with Docker and GitHub Actions CI/CD",
    version="1.0.0",
)

app.include_router(health.router)
app.include_router(items.router, prefix="/api/v1")
