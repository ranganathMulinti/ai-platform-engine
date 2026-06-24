from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """
    Define the lifespan events for the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """

    # Startup event
    async def startup() -> None:
        print("Application is starting up")

    # Shutdown event
    async def shutdown() -> None:
        print("Application is shutting down")

    await startup()
    yield
    await shutdown()
