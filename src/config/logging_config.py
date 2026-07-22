import logging

from src.logging.request_context_filter import RequestContextFilter

def configure_logging():
    handler = logging.StreamHandler()
    handler.addFilter(RequestContextFilter())

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(request_id)s] %(name)s - %(message)s",
        handlers=[handler]
    )
