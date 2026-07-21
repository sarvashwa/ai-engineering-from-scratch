import logging
import time

logger = logging.getLogger(__name__)

class Timer:
    def __init__(self, operation: str):
        self.operation = operation

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, *_):
        elapsed = (time.perf_counter() - self.start) * 1000
        logger.info(f"{self.operation} took {elapsed:.2f} ms")