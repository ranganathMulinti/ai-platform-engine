"""
Vector store schemas.
"""

from pydantic import BaseModel


class VectorRecord(BaseModel):
    """
    Record stored in a vector database.
    """

    document_id: int

    chunk_index: int

    text: str

    embedding: list[float]
