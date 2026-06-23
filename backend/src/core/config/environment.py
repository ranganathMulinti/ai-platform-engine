# environment.py

from .settings import Settings


def get_environment_settings() -> Settings:
    """
    Retrieve environment-specific configuration settings.

    Returns:
        Settings: The environment-specific settings.
    """
    return Settings()
