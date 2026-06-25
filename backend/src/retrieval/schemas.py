"""
Retrieval schemas.
"""

from pydantic import BaseModel


class RetrievedChunk(BaseModel):
    """
    Retrieved chunk.
    """

    document_id: int

    chunk_index: int

    text: str

    score: float


class RetrievalResult(BaseModel):
    """
    Retrieval response.
    """

    chunks: list[RetrievedChunk]
