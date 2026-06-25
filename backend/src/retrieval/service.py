"""
Retriever implementation.
"""

from embeddings.service import (
    SentenceTransformerEmbeddingProvider,
)
from retrieval.base import Retriever
from retrieval.constants import DEFAULT_TOP_K
from retrieval.schemas import (
    RetrievalResult,
    RetrievedChunk,
)
from vectorstore.service import VectorStoreService


class VectorRetriever(Retriever):
    """
    Vector search retriever.
    """

    def __init__(
        self,
        vector_store: VectorStoreService,
    ) -> None:
        self.vector_store = vector_store

        self.embedding_provider = SentenceTransformerEmbeddingProvider()

    def retrieve(
        self,
        query: str,
        top_k: int = DEFAULT_TOP_K,
    ) -> RetrievalResult:
        """
        Retrieve relevant chunks.
        """

        embedding = self.embedding_provider.model.encode(
            query,
            normalize_embeddings=True,
        ).tolist()

        results = self.vector_store.search(
            embedding,
            top_k,
        )

        chunks = [
            RetrievedChunk(
                document_id=item.document_id,
                chunk_index=item.chunk_index,
                text=item.text,
                score=0.0,
            )
            for item in results
        ]

        return RetrievalResult(
            chunks=chunks,
        )
