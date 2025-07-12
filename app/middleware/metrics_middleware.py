import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from ..metrics.http_metrics import (
    HTTP_REQUESTS_TOTAL, HTTP_REQUESTS_LATENCY_SECONDS,
    HTTP_REQUESTS_SIZE_BYTES, HTTP_RESPONSES_SIZE_BYTES
)


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        method = request.method
        path = request.url.path

        request_body = await request.body()
        HTTP_REQUESTS_SIZE_BYTES.labels(method=method, path=path).observe(len(request_body))

        try:
            response: Response = await call_next(request)
            body = b""
            try:
                async for chunk in response.body_iterator:
                    body += chunk
            except Exception as e:
                print("Error while reading response body: %s", str(e))
                body = b""

            duration = time.time() - start
            HTTP_REQUESTS_LATENCY_SECONDS.labels(method=method, path=path).observe(duration)
            HTTP_REQUESTS_TOTAL.labels(method=method, path=path, status_code=response.status_code).inc()
            HTTP_RESPONSES_SIZE_BYTES.labels(method=method, path=path).observe(len(body))

            return Response(
                content=body,
                status_code=response.status_code,
                headers=dict(response.headers.items()),  # ✅ safe copy
                media_type=response.media_type
            )

        except Exception as e:
            print("Unhandled error in middleware: %s", str(e))
            raise


