"""
Retriever interface.
"""

from abc import ABC, abstractmethod

from retrieval.schemas import RetrievalResult


class Retriever(ABC):
    """
    Base retriever.
    """

    @abstractmethod
    def retrieve(
        self,
        query: str,
        top_k: int,
    ) -> RetrievalResult:
        """
        Retrieve relevant chunks.
        """
