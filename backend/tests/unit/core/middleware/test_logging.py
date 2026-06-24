from unittest.mock import patch

from core.middleware.logging import logger
from fastapi.testclient import TestClient
from main import create_app

client = TestClient(create_app())


@patch.object(logger, "info")
def test_logging_middleware(mock_logger):
    response = client.get("/health/live")

    assert response.status_code == 200

    mock_logger.assert_called_once()


def test_response_unchanged():
    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "alive"}
