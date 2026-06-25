"""
Tool schemas.
"""

from pydantic import BaseModel


class ToolRequest(BaseModel):
    """
    Tool execution request.
    """

    tool: str

    arguments: dict[str, object]


class ToolResponse(BaseModel):
    """
    Tool execution response.
    """

    output: str
