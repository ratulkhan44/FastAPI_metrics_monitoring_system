from fastapi import FastAPI
from prometheus_client import make_asgi_app
from .routers import health
from .middleware.metrics_middleware import MetricsMiddleware
from .metrics.system_metrics import start_system_metric_collector

app = FastAPI(
    title="FastAPI Metrics Monitoring System",
    description="Monitors system and HTTP metrics for Prometheus"
)

# Include routers
app.include_router(health.router, tags=["Health"])

# Add Prometheus custom middleware
app.add_middleware(MetricsMiddleware)

# Mount /metrics endpoint for Prometheus scraping
app.mount("/metrics", make_asgi_app())

# Start system metrics background task
@app.on_event("startup")
async def startup_event():
    start_system_metric_collector()