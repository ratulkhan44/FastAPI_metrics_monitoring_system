# FastAPI Metrics Monitoring System

A production-ready FastAPI app for system and HTTP metrics observability with Prometheus integration.

---

## Features

- **System Metrics:** CPU, memory, file descriptors, threads, application uptime.
- **Request Metrics:** Request/response count, volume, latency, request/response sizes.
- **/metrics Endpoint:** Prometheus-compatible system and application metrics.
- **Docker Ready:** Easy deployment using Docker Compose.
- **Liveness/Readiness Route:** `/health` endpoint for fast health checks.

---

## Quickstart

**Requirements:**  
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)

**Instructions:**
```bash
git clone https://github.com/ratulkhan44/FastAPI_metrics_monitoring_system.git
cd FastAPI_metrics_monitoring_system
docker compose up --build


## 🚦 Available Endpoints List

| URL                            | Description                        |
|--------------------------------|------------------------------------|
| http://localhost:8000/health   | Health check endpoint              |
| http://localhost:8000/metrics  | Prometheus metrics endpoint        |
| http://localhost:9090/         | Prometheus dashboard (PromQL UI)   |

