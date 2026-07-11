from fastapi import APIRouter, status, Depends

from src.api.schemas.health_response import HealthResponse
from src.application.application import Application
from src.api.dependencies import get_application

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get(
        "",
        response_model=HealthResponse,
        status_code=status.HTTP_200_OK,
        summary="Check Application Health",
        description="Returns the current health status and version of the application.Returns the current health status and version of the application.",
        )
def get_health(
    application: Application = Depends(get_application)
) -> HealthResponse:
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        active=1
    )