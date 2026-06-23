# test_interfaces.py

import pytest
from core.config.interfaces import ConfigLoader, ConfigValidator
from core.config.types import ConfigType


class MockConfigLoader(ConfigLoader):
    def load(self) -> ConfigType:
        return "mock_config"


class MockConfigValidator(ConfigValidator):
    def validate(self, config: ConfigType) -> None:
        pass


def test_interfaces():
    # Test ConfigLoader interface
    loader = MockConfigLoader()
    assert loader.load() == "mock_config"

    # Test ConfigValidator interface
    validator = MockConfigValidator()
    validator.validate("config")
