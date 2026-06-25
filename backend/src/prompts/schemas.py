"""
Prompt schemas.
"""

from pydantic import BaseModel


class Prompt(BaseModel):
    """
    Prompt definition.
    """

    name: str

    version: str

    template: str


class PromptRenderRequest(BaseModel):
    """
    Prompt rendering request.
    """

    name: str

    variables: dict[str, str]


class PromptRenderResponse(BaseModel):
    """
    Rendered prompt.
    """

    prompt: str
