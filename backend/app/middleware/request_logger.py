import uuid
from time import time

from flask import Flask, g, request


def init_request_logger(app: Flask) -> None:
    @app.before_request
    def before_request() -> None:
        g.correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
        g.start_time = time()
        app.logger.info(
            "Request: %s %s [%s]",
            request.method,
            request.path,
            g.correlation_id,
        )

    @app.after_request
    def after_request(response) -> None:
        duration = time() - g.get("start_time", time())
        app.logger.info(
            "Response: %s %s -> %d (%.3fs) [%s]",
            request.method,
            request.path,
            response.status_code,
            duration,
            g.correlation_id,
        )
        response.headers["X-Correlation-ID"] = g.get("correlation_id", "")
        return response
