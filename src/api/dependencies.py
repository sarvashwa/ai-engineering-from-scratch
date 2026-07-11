from fastapi import Request, Depends

from src.application.application import Application

def get_application(request: Request) -> Application:
    return request.app.state.application

def get_rag_service(
        application: Application = Depends(get_application)
        ) -> Application:
    return application.rag_service