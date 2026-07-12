from fastapi import FastAPI

from src.api.router import router
from src.application.bootstrap import create_application
from src.api.middleware import register_middleware
from src.config.logging_config import configure_logging
from src.api.exception_handlers import register_exception_handlers
from src.api.lifespan import lifespan

configure_logging()

app = FastAPI(
    title="AI Engineering From Scratch",
    version="1.0.0",
    lifespan=lifespan
)

register_middleware(app)

register_exception_handlers(app)

app.include_router(router)