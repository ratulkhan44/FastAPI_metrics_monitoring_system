from prometheus_client import Counter, Histogram, Summary

HTTP_REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status_code"]
)
HTTP_REQUESTS_LATENCY_SECONDS = Histogram(
    "http_requests_latency_seconds",
    "HTTP request latency",
    ["method", "path"]
)
HTTP_REQUESTS_SIZE_BYTES = Summary(
    "http_request_size_bytes",
    "Size of HTTP requests",
    ["method", "path"]
)
HTTP_RESPONSES_SIZE_BYTES = Summary(
    "http_response_size_bytes",
    "Size of HTTP responses",
    ["method", "path"]
)