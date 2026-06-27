# 🔗 URL Shortener — DevOps Portfolio Project

![CI/CD](https://github.com/lukemadeit09/url-shortener/actions/workflows/ci.yml/badge.svg)

A working URL shortener (Flask + Redis), built as a **progressive DevOps project**. Each phase wraps the app in a new layer of real-world DevOps tooling — from local containers all the way to a self-healing Kubernetes deployment with an automated CI/CD pipeline.

Built hands-on, phase by phase, to learn the full DevOps stack.

---

## What it does

- Paste a long URL → get a short code back.
- Visit the short code → get redirected to the original URL.
- Short codes are stored in Redis.
- `/health` endpoint for health checks.

---

## Tech stack

| Layer | Tech |
|---|---|
| App | Python (Flask) |
| Data store | Redis |
| Containers | Docker, Docker Compose |
| CI/CD | GitHub Actions (test → build → publish to GHCR) |
| Infrastructure as Code | Terraform |
| Orchestration | Kubernetes (Deployments, Services, self-healing, scaling) |
| Monitoring | Prometheus + Grafana *(next)* |

---

## Roadmap

- [x] **Phase 1 — Containerized app.** Flask + Redis, Dockerfile, Docker Compose, unit tests.
- [x] **Phase 2 — CI.** GitHub Actions runs the test suite automatically on every push.
- [x] **Phase 3 — Infrastructure as Code.** Terraform provisions resources (developed and validated against LocalStack).
- [x] **Phase 4 — CD.** Pipeline builds the Docker image and publishes it to GitHub Container Registry on every green build.
- [x] **Phase 5 — Kubernetes.** Deployed to a K8s cluster with multiple replicas, load balancing, self-healing, and horizontal scaling.
- [ ] **Phase 6 — Observability.** Metrics and dashboards with Prometheus + Grafana.
- [ ] **Phase 7 — DevSecOps.** Image scanning, secret scanning, and secure pipelines.

---

## Run it locally (Docker Compose)

Requires [Docker Desktop](https://www.docker.com/products/docker-desktop/).

```bash
docker compose up --build
```

Open http://localhost:8080, paste a URL, and shorten it. Stop with `docker compose down`.

---

## Run the tests

```bash
docker compose exec web python -m pytest
```

---

## Infrastructure as Code (Terraform)

The `terraform/` folder defines infrastructure as code. Developed against LocalStack (a free local AWS emulator), so it runs at zero cost.

```bash
cd terraform
terraform init
terraform plan
terraform apply      # creates the resources
terraform destroy    # tears them down cleanly
```

---

## Deploy to Kubernetes

The `k8s/` folder contains the Deployment and Service manifests for the app and Redis.

```bash
kubectl apply -f k8s/
kubectl get pods                                  # 1 redis + 2 web pods
kubectl port-forward service/web 8080:8080        # access at http://localhost:8080
```

Features demonstrated:
- **Self-healing** — kill a pod (`kubectl delete pod <name>`) and Kubernetes recreates it automatically.
- **Scaling** — `kubectl scale deployment web --replicas=4`.

Tear down with `kubectl delete -f k8s/`.

---

## CI/CD pipeline

On every push to `main`, GitHub Actions:
1. Runs the test suite (pytest).
2. **Only if tests pass**, builds the Docker image and publishes it to `ghcr.io/lukemadeit09/url-shortener:latest`.

See `.github/workflows/ci.yml`.

---

## Architecture

```
        ┌──────────────┐         ┌──────────────┐
Browser │   web (Flask)│ ──────▶ │    redis     │
        │  2 replicas  │  store/ │              │
        │  port 5000   │  lookup │  port 6379   │
        └──────────────┘         └──────────────┘
     load-balanced by a Kubernetes Service
```

---

## Author

Built by Luke — a hands-on journey through the full DevOps stack: containers, CI/CD, Infrastructure as Code, and Kubernetes.
