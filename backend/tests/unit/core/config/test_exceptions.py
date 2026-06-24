import pytest
from core.config import ConfigurationError


def test_configuration_error():
    with pytest.raises(ConfigurationError):
        raise ConfigurationError("Test error")
