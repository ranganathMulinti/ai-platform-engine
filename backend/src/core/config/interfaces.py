# interfaces.py

from typing import Protocol
from .types import ConfigType  # Import ConfigType alias


class ConfigLoader(Protocol):
    """
    Interface for loading configuration settings.
    """

    def load(self) -> "ConfigType":
        ...


class ConfigValidator(Protocol):
    """
    Interface for validating configuration settings.
    """

    def validate(self, config: "ConfigType") -> None:
        ...
