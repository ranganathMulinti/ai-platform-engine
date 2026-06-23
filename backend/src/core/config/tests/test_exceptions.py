# test_exceptions.py

import pytest
from core.config.exceptions import ConfigError


def test_config_error():
    # Test ConfigError exception
    with pytest.raises(ConfigError):
        raise ConfigError("Test error")
