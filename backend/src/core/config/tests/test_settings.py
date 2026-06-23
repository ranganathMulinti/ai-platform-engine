# test_settings.py

import pytest
from core.config.settings import Settings


def test_settings():
    # Test default values
    settings = Settings()
    assert settings.debug_mode is False

    # Test environment variables
    with pytest.raises(ValueError):
        Settings(database_url="test_db", secret_key="test_secret")
