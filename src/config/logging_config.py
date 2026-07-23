import logging

from src.logging.request_context_filter import RequestContextFilter
from src.logging.josn_formatter import JsonFormatter

def configure_logging():
    handler = logging.StreamHandler()

    handler.addFilter(RequestContextFilter())

    formatter = JsonFormatter()
    handler.setFormatter(formatter)

    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler]
        # format is now updated to be used from JSONFormatter
        # format="%(asctime)s %(levelname)s [%(request_id)s] %(name)s - %(message)s",
    )
