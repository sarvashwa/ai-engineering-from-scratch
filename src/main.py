from fastapi import FastAPI

from src.api.router import router
from src.application.bootstrap import create_application
from src.api.middleware import register_middleware
from src.config.logging_config import configure_logging
from src.api.exception_handlers import register_exception_handlers
from src.config.config import load_settings

settings = load_settings()

configure_logging()

application = create_application(
    settings=settings
)

app = FastAPI(
    title="AI Engineering From Scratch",
    version="1.0.0",
)

register_middleware(app)

register_exception_handlers(app)

app.state.application = application

app.include_router(router)