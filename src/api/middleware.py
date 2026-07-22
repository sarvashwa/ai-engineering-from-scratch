import time
import logging
import uuid

from fastapi import FastAPI, Request

from src.context.request_context import set_request_id


logger = logging.getLogger(__name__)

def register_middleware(app: FastAPI) -> None:

    @app.middleware("http")
    async def request_timer(request: Request, call_next):

        start = time.perf_counter()

        request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        set_request_id(request_id)
        request.state.request_id = request_id

        logger.info(f"--> {request.method} {request.url.path}")

        try:
            response = await call_next(request)

            elapsed = (time.perf_counter() - start) * 1000

            logger.info(f"<-- {request.method} {request.url.path} ({elapsed:.2f} ms)")

            return response
        finally:
            set_request_id(None)