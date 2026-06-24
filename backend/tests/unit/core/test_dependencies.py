from core.dependencies import get_health_service, get_settings
from core.health.service import HealthService


def test_get_settings_returns_same_instance():
    """
    Test that get_settings() returns the same Settings instance every call.
    """
    settings1 = get_settings()
    settings2 = get_settings()
    assert settings1 is settings2


def test_get_health_service_returns_new_instance():
    """
    Test that get_health_service() returns a HealthService instance.
    """
    health_service = get_health_service()
    assert isinstance(health_service, HealthService)
