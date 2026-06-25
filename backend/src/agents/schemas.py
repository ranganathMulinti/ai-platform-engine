"""
Agent schemas.
"""

from pydantic import BaseModel


class AgentRequest(BaseModel):
    """
    Agent request.
    """

    message: str


class AgentResponse(BaseModel):
    """
    Agent response.
    """

    answer: str
