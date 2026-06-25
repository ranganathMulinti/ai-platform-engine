"""
Tool service.
"""

from tools.registry import ToolRegistry
from tools.schemas import (
    ToolRequest,
    ToolResponse,
)


class ToolService:
    """
    Tool execution service.
    """

    def __init__(
        self,
        registry: ToolRegistry,
    ) -> None:
        self.registry = registry

    def execute(
        self,
        request: ToolRequest,
    ) -> ToolResponse:
        """
        Execute a tool.
        """

        tool = self.registry.get(
            request.tool,
        )

        return tool.execute(
            request,
        )
