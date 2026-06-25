"""
Vector store service.
"""

from vectorstore.base import VectorStore
from vectorstore.schemas import VectorRecord


class VectorStoreService:
    """
    Application service.
    """

    def __init__(
        self,
        provider: VectorStore,
    ) -> None:
        self.provider = provider

    def upsert(
        self,
        records: list[VectorRecord],
    ) -> None:
        self.provider.upsert(records)

    def search(
        self,
        embedding: list[float],
        top_k: int,
    ) -> list[VectorRecord]:
        return self.provider.search(
            embedding,
            top_k,
        )
