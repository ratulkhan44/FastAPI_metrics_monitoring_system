# FastAPI Metrics Monitoring System

A production-ready FastAPI app for system and HTTP metrics observability with Prometheus integration.

## Features

- System metrics: CPU, memory, file descriptors, threads, uptime
- Request metrics: volume, latency, request/response sizes
- `/metrics` Prometheus endpoint
- Docker-ready, easy deployment

## Quickstart

```bash
git clone <repo>
cd fastapi-metrics
docker-compose up --build