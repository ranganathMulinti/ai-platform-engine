"""
Embedding service.
"""

from chunking.schemas import DocumentChunk
from embeddings.base import EmbeddingProvider
from embeddings.constants import DEFAULT_EMBEDDING_MODEL
from embeddings.schemas import EmbeddedChunk
from sentence_transformers import SentenceTransformer


class SentenceTransformerEmbeddingProvider(
    EmbeddingProvider,
):
    """
    SentenceTransformer implementation.
    """

    def __init__(
        self,
    ) -> None:
        self.model = SentenceTransformer(
            DEFAULT_EMBEDDING_MODEL,
        )

    def embed(
        self,
        chunks: list[DocumentChunk],
    ) -> list[EmbeddedChunk]:
        texts = [chunk.text for chunk in chunks]

        vectors = self.model.encode(
            texts,
            normalize_embeddings=True,
        )

        embedded_chunks: list[EmbeddedChunk] = []

        for chunk, vector in zip(
            chunks,
            vectors,
            strict=True,
        ):
            embedded_chunks.append(
                EmbeddedChunk(
                    chunk_index=chunk.chunk_index,
                    text=chunk.text,
                    embedding=vector.tolist(),
                )
            )

        return embedded_chunks
