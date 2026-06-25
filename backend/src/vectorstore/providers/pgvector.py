"""
pgvector provider.

Implementation comes in the next batch.
"""

from vectorstore.base import VectorStore
from vectorstore.schemas import VectorRecord


class PgVectorStore(VectorStore):
    """
    pgvector implementation.
    """

    def upsert(
        self,
        records: list[VectorRecord],
    ) -> None:
        raise NotImplementedError

    def search(
        self,
        embedding: list[float],
        top_k: int,
    ) -> list[VectorRecord]:
        raise NotImplementedError
