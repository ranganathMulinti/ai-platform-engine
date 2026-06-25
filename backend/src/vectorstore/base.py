"""
Vector store interface.
"""

from abc import ABC, abstractmethod

from vectorstore.schemas import VectorRecord


class VectorStore(ABC):
    """
    Base vector store.
    """

    @abstractmethod
    def upsert(
        self,
        records: list[VectorRecord],
    ) -> None:
        """
        Insert or update vectors.
        """

    @abstractmethod
    def search(
        self,
        embedding: list[float],
        top_k: int,
    ) -> list[VectorRecord]:
        """
        Similarity search.
        """
