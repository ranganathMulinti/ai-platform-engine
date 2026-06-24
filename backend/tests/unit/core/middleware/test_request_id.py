import uuid

from core.middleware.request_id import RequestIdMiddleware
from fastapi.testclient import TestClient
from main import create_app

app = create_app()
app.add_middleware(RequestIdMiddleware)

client = TestClient(app)


def test_request_id_header_exists():
    """
    Test that the X-Request-ID header exists in the response.
    """
    response = client.get("/")
    assert "X-Request-ID" in response.headers


def test_request_id_is_valid_uuid():
    """
    Test that the X-Request-ID header value is a valid UUID.
    """
    response = client.get("/")
    request_id = response.headers["X-Request-ID"]
    try:
        uuid.UUID(request_id)
    except ValueError as exc:
        raise AssertionError("X-Request-ID is not a valid UUID") from exc


def test_each_request_has_unique_id():
    """
    Test that each request gets a different UUID.
    """
    response1 = client.get("/")
    response2 = client.get("/")
    assert response1.headers["X-Request-ID"] != response2.headers["X-Request-ID"]
