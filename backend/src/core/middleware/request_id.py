import uuid

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


class RequestIdMiddleware(BaseHTTPMiddleware):
    """
    Middleware to generate and propagate a unique request ID for each incoming request.
    """

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """
        Generate a UUID4 for the request, store it in request.state.request_id,
        and add it to the response header X-Request-ID.

        Args:
            request (Request): The incoming request.
            call_next (RequestResponseEndpoint): The next endpoint to call.

        Returns:
            Response: The response with the X-Request-ID header.
        """
        request_id = str(uuid.uuid4())

        request.state.request_id = request_id

        response = await call_next(request)

        response.headers["X-Request-ID"] = request_id

        return response
