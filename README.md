# cloud-fastapi-demo

[![CI](https://github.com/CarlosRolo/cloud-fastapi-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/CarlosRolo/cloud-fastapi-demo/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Containerized REST API built with FastAPI, optimized multi-stage Docker build, and automated CI/CD pipeline using GitHub Actions that lints, tests, and publishes to GitHub Container Registry on every push.

## Features

- FastAPI with Pydantic v2 validation
- Optimized multi-stage Dockerfile (builder + runtime stages)
- Docker Compose for dev (hot reload) and prod environments
- GitHub Actions pipeline: lint → test → build → push to GHCR
- Non-root container user for security
- Built-in healthcheck endpoint

## Quick Start

```bash
# Development (hot reload)
docker compose up --build

# Pull and run production image
docker pull ghcr.io/carlosrolo/cloud-fastapi-demo:latest
docker run -p 8000:8000 ghcr.io/carlosrolo/cloud-fastapi-demo:latest
```

API available at http://localhost:8000/docs

## Project Structure

cloud-fastapi-demo/
├── app/
│   ├── main.py          # App entry point
│   ├── schemas.py       # Pydantic models
│   └── routers/         # Route handlers
├── tests/               # pytest test suite
├── .github/workflows/   # GitHub Actions CI/CD
├── Dockerfile           # Multi-stage build
└── docker-compose.yml   # Dev orchestration

## CI/CD Pipeline

Every push to `main` triggers:
1. **Lint** — ruff + black format check
2. **Test** — pytest with httpx async client
3. **Build & Push** — multi-stage image published to GHCR

## Author

**Carlos David Rodriguez Lopez**  
Telematic Engineer — ESPOCH  
Riobamba, Chimborazo, Ecuador  
Manta, Manabí, Ecuador  
GitHub: [github.com/CarlosRolo](https://github.com/CarlosRolo)  
LinkedIn: [linkedin.com/in/carlosdrodriguezl](https://linkedin.com/in/carlosdrodriguezl)

## License

MIT License — see [LICENSE](LICENSE)
