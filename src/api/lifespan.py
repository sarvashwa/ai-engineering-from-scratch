from contextlib import asynccontextmanager
from fastapi import FastAPI
from collections.abc import AsyncIterator

from src.application.bootstrap import create_application
from src.config.config import load_settings

settings = load_settings()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:

    application = create_application(settings)

    app.state.application = application

    yield

    application.shutdown()