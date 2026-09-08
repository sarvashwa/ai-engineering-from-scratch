from fastapi import Request

from src.application.application import Application

def get_application(request: Request) -> Application:
    return request.app.state.application
