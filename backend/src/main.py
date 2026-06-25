from auth.router import router as auth_router
from core.config.settings import Settings
from core.exceptions.handlers import (
    register_exception_handlers,
)
from core.health.router import router as health_router
from core.lifespan import lifespan
from core.middleware.logging import LoggingMiddleware
from core.middleware.request_id import RequestIdMiddleware
from fastapi import FastAPI


def create_app() -> FastAPI:
    """
    Create and configure a FastAPI application.

    Returns:
        FastAPI: The configured FastAPI application.
    """
    settings = Settings()
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        lifespan=lifespan,
    )
    register_exception_handlers(app)
    app.include_router(health_router)
    app.include_router(auth_router)
    # Infrastructure middleware
    app.add_middleware(RequestIdMiddleware)
    app.add_middleware(LoggingMiddleware)
    return app


app = create_app()
