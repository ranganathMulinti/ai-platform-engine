"""
RAG schemas.
"""

from pydantic import BaseModel


class RAGRequest(BaseModel):
    """
    User question.
    """

    question: str

    top_k: int = 5


class RAGResponse(BaseModel):
    """
    Generated response.
    """

    answer: str

    context: list[str]
