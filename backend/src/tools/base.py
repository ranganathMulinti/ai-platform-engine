"""
Base tool interface.
"""

from abc import ABC, abstractmethod

from tools.schemas import (
    ToolRequest,
    ToolResponse,
)


class Tool(ABC):
    """
    Base tool.
    """

    name: str
    description: str

    @abstractmethod
    def execute(
        self,
        request: ToolRequest,
    ) -> ToolResponse:
        """
        Execute the tool.
        """
