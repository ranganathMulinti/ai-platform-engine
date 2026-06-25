"""
LLM schemas.
"""

from pydantic import BaseModel


class GenerationRequest(BaseModel):
    """
    Text generation request.
    """

    prompt: str

    temperature: float = 0.2

    max_tokens: int = 2048


class GenerationResponse(BaseModel):
    """
    LLM response.
    """

    text: str
