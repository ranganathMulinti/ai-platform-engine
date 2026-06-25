"""
Embedding schemas.
"""

from pydantic import BaseModel


class EmbeddedChunk(BaseModel):
    """
    Embedded document chunk.
    """

    chunk_index: int

    text: str

    embedding: list[float]
