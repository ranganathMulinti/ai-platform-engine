"""
Global exception handlers.
"""

from core.exceptions.base import AppException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def register_exception_handlers(
    app: FastAPI,
) -> None:
    """
    Register application exception handlers.
    """

    @app.exception_handler(AppException)
    async def app_exception_handler(
        request: Request,
        exc: AppException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.detail,
            },
        )
