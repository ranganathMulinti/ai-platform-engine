# test_validators.py

import pytest
from core.config.validators import validate_config
from core.config.types import ConfigType
from core.config.settings import Settings
from core.config.exceptions import ConfigError  # Import ConfigError class


def test_validate_config():
    # Test valid configuration
    config = Settings(database_url="test_db", secret_key="test_secret")
    validate_config(config)

    # Test invalid configuration type
    with pytest.raises(ConfigError):
        validate_config("invalid_config")
