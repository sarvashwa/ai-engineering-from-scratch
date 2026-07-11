import time
import logging

from fastapi import FastAPI, Request

logger = logging.getLogger(__name__)

def register_middleware(app: FastAPI) -> None:

    @app.middleware("http")
    async def request_timer(request: Request, call_next):

        start = time.perf_counter()

        logger.info(f"--> {request.method} {request.url.path}")

        response = await call_next(request)

        elapsed = (time.perf_counter() - start) * 1000

        logger.info(f"<-- {request.method} {request.url.path} ({elapsed:.2f} ms)")

        return response