"""
Chunking interface.
"""

from abc import ABC, abstractmethod

from chunking.schemas import DocumentChunk


class Chunker(ABC):
    """
    Base chunker.
    """

    @abstractmethod
    def chunk(
        self,
        text: str,
    ) -> list[DocumentChunk]:
        """
        Split text into chunks.
        """
