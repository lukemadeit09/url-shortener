# 🔗 URL Shortener — DevOps Portfolio Project

A working URL shortener (Flask + Redis), built as a progressive DevOps project. Each phase wraps the app in a new layer of real-world DevOps tooling — from local containers to a monitored cloud deployment.

## What it does
- Paste a long URL → get a short code back.
- Visit the short code → redirected to the original URL.
- Short codes stored in Redis. `/health` endpoint for health checks.

## Tech stack
| Layer | Tech |
|---|---|
| App | Python (Flask) |
| Data store | Redis |
| Containers | Docker, Docker Compose |
| CI/CD | GitHub Actions *(Phase 2)* |
| IaC | Terraform *(Phase 3)* |
| Cloud | AWS *(Phase 4)* |
| Orchestration | Kubernetes *(Phase 5)* |
| Monitoring | Prometheus + Grafana *(Phase 6)* |

## Roadmap
- [x] Phase 1 — Containerized app (Flask + Redis, Docker, Compose, tests)
- [x] Phase 2 — CI/CD with GitHub Actions
- [ ] Phase 3 — Infrastructure as Code (Terraform)
- [ ] Phase 4 — Deploy to AWS
- [ ] Phase 5 — Kubernetes
- [ ] Phase 6 — Monitoring (Prometheus + Grafana)

## Run it locally
Requires Docker Desktop.
```bash

docker compose up --build

```
Then open http://localhost:8080

## Run the tests
```bash

docker compose exec web python -m pytest

```

Built by Luke as a hands-on journey through the DevOps stack.