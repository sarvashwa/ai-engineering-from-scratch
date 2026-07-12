from fastapi import APIRouter, status, Depends, BackgroundTasks

from src.api.background_log import background_log
from src.api.dependencies import get_rag_service
from src.services.rag_service import RAGService
from src.api.schemas.ask_request import AskRequest
from src.api.schemas.ask_response import AskResponse

router = APIRouter(
    prefix="/ask",
    tags=["RAG"]
)

@router.post(
        "",
        response_model=AskResponse,
        summary="Ask a question",
        status_code=status.HTTP_200_OK,
        description=(
        "Accepts a user question, forwards it to the RAG service, "
        "and returns an AI-generated answer."
        ),
)
def ask(
    request: AskRequest,
    rag_service: RAGService = Depends(get_rag_service),
    ):
    answer = rag_service.answer(
        question=request.question,
        top_k=request.top_k
    )

    return AskResponse (
        answer = answer
    )

@router.post("/background-test")
def background_test(
    background_tasks: BackgroundTasks,
):
    background_tasks.add_task(background_log)

    return {
        "message": "Response returned immediately."
    }