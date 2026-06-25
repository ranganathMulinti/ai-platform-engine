"""
Chunking service.
"""

from chunking.base import Chunker
from chunking.constants import (
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_CHUNK_SIZE,
)
from chunking.schemas import DocumentChunk


class RecursiveCharacterChunker(Chunker):
    """
    Character-based chunker.
    """

    def __init__(
        self,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
    ) -> None:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(
        self,
        text: str,
    ) -> list[DocumentChunk]:
        chunks: list[DocumentChunk] = []

        start = 0

        index = 0

        while start < len(text):
            end = min(
                start + self.chunk_size,
                len(text),
            )

            chunks.append(
                DocumentChunk(
                    chunk_index=index,
                    text=text[start:end],
                    start_offset=start,
                    end_offset=end,
                )
            )

            if end == len(text):
                break

            start = end - self.chunk_overlap

            index += 1

        return chunks
