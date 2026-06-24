from core.config.settings import Settings
from core.health.service import HealthService

_settings_instance = None


def get_settings() -> Settings:
    """
    Dependency provider function to return a singleton Settings instance.

    Returns:
        Settings: The singleton Settings instance.
    """
    global _settings_instance
    if _settings_instance is None:
        _settings_instance = Settings()
    return _settings_instance


def get_health_service() -> HealthService:
    """
    Dependency provider function to return a HealthService instance.

    Returns:
        HealthService: A new HealthService instance.
    """
    return HealthService()
