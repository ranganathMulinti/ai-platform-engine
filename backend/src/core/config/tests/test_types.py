# test_types.py

import pytest
from core.config.types import ConfigType


def test_types():
    # Test ConfigType alias
    assert ConfigType == "Settings"
