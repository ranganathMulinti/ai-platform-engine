"""
Embedding interface.
"""

from abc import ABC, abstractmethod

from chunking.schemas import DocumentChunk
from embeddings.schemas import EmbeddedChunk


class EmbeddingProvider(ABC):
    """
    Base embedding provider.
    """

    @abstractmethod
    def embed(
        self,
        chunks: list[DocumentChunk],
    ) -> list[EmbeddedChunk]:
        """
        Generate embeddings.
        """
