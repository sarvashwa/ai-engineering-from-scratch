import logging

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse


from src.exceptions.exceptions import DocumentNotFoundException

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