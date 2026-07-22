import logging
import time

from src.context.request_context import get_request_id


logger = logging.getLogger(__name__)

class Timer:
    def __init__(self, operation: str):
        self.operation = operation

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, *_):
        request_id = get_request_id() or "-"

        elapsed = (time.perf_counter() - self.start) * 1000
        logger.info(f"[{request_id}] {self.operation} took {elapsed:.2f} ms")