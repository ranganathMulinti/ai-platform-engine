# loader.py

from .settings import Settings
from .environment import get_environment_settings
from .types import ConfigType
from .validators import validate_config
from .exceptions import ConfigError


def load_config() -> ConfigType:
    """
    Load the configuration settings.

    Returns:
        ConfigType: The loaded configuration.
    """
    try:
        config = get_environment_settings()
        validate_config(config)
        return config
    except Exception as e:
        raise ConfigError(f"Failed to load configuration: {e}")
