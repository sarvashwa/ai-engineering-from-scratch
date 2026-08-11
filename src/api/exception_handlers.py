import logging

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

from src.exceptions.document_not_found_exceptions import DocumentNotFoundException
from src.exceptions.user_not_found_exception import UserNotFoundException

def register_exception_handlers(app: FastAPI):
    logger = logging.getLogger(__name__)

    @app.exception_handler(Exception)
    def handle_exception(request: Request, exception: Exception):

        logger.exception("Unexpected error")
        # alternatively we can use
        # logger.error(
        #  "Unexpected error",
        #  exc_info=True
        # )
        # 
        return JSONResponse(
            status_code=500,
            content={
                "detail": "Internal Server Error"
            }
        )

    @app.exception_handler(DocumentNotFoundException)
    def handle_document_not_found(
        request: Request,
        exception: DocumentNotFoundException,
    ):
        logger.warning(str(exception))
        return JSONResponse(
            status_code=404,
            content={
                "detail": str(exception)
            }
        )

    @app.exception_handler(UserNotFoundException)
    def handle_user_not_found(
        request: Request,
        exception: UserNotFoundException,
    ):
        logger.warning(str(exception))
        return JSONResponse(
            status_code=404,
            content={
                "detail": str(exception)
            }
        )