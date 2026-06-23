# validators.py

from .settings import Settings
from .types import ConfigType
from .exceptions import ConfigError


def validate_config(config: ConfigType) -> None:
    """
    Validate the configuration settings.

    Args:
        config (ConfigType): The configuration to validate.

    Raises:
        ConfigError: If the configuration is invalid.
    """
    if not isinstance(config, Settings):
        raise ConfigError("Invalid configuration type")

    # Add additional validation logic here
