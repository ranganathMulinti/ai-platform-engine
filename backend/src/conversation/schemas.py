"""
Conversation schemas.
"""

from pydantic import BaseModel


class ChatMessage(BaseModel):
    """
    Chat message.
    """

    role: str

    content: str


class ChatRequest(BaseModel):
    """
    Chat request.
    """

    conversation_id: str

    message: str


class ChatResponse(BaseModel):
    """
    Chat response.
    """

    answer: str

    messages: list[ChatMessage]
