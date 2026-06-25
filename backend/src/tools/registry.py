"""
Tool registry.
"""

from tools.base import Tool
from tools.exceptions import ToolNotFoundException


class ToolRegistry:
    """
    Registry of available tools.
    """

    def __init__(
        self,
    ) -> None:
        self._tools: dict[str, Tool] = {}

    def register(
        self,
        tool: Tool,
    ) -> None:
        """
        Register a tool.
        """

        self._tools[tool.name] = tool

    def get(
        self,
        name: str,
    ) -> Tool:
        """
        Retrieve a tool.
        """

        tool = self._tools.get(
            name,
        )

        if tool is None:
            raise ToolNotFoundException()

        return tool

    def list(
        self,
    ) -> list[str]:
        """
        List registered tools.
        """

        return sorted(
            self._tools.keys(),
        )
