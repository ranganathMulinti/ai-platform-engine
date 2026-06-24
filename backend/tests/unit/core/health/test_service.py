from core.health.schemas import HealthResponse
from core.health.service import HealthService


def test_get_liveness():
    """
    Test the get_liveness method of HealthService.
    """
    service = HealthService()
    response = service.get_liveness()
    assert isinstance(response, HealthResponse)
    assert response.status == "alive"


def test_get_readiness():
    """
    Test the get_readiness method of HealthService.
    """
    service = HealthService()
    response = service.get_readiness()
    assert isinstance(response, HealthResponse)
    assert response.status == "ready"
