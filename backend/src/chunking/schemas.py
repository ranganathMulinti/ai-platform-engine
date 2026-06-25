"""
Chunking schemas.
"""

from pydantic import BaseModel


class DocumentChunk(BaseModel):
    """
    A single document chunk.
    """

    chunk_index: int

    text: str

    start_offset: int

    end_offset: int
