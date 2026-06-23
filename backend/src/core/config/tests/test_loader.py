# test_loader.py

import pytest
from core.config.loader import load_config
from core.config.settings import Settings  # Import Settings class


def test_load_config():
    # Test loading configuration
    config = load_config()
    assert isinstance(config, Settings)
