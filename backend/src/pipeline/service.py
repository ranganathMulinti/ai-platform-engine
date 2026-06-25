"""
Ingestion pipeline.
"""

from pathlib import Path

from chunking.service import RecursiveCharacterChunker
from embeddings.service import (
    SentenceTransformerEmbeddingProvider,
)
from ingestion.schemas import IngestionRequest
from ingestion.service import IngestionService
from pipeline.schemas import (
    IngestionPipelineRequest,
    IngestionPipelineResponse,
)
from vectorstore.schemas import VectorRecord
from vectorstore.service import VectorStoreService


class IngestionPipeline:
    """
    Complete ingestion pipeline.
    """

    def __init__(
        self,
        vector_store: VectorStoreService,
    ) -> None:
        self.ingestion = IngestionService()

        self.chunker = RecursiveCharacterChunker()

        self.embedding = SentenceTransformerEmbeddingProvider()

        self.vector_store = vector_store

    def execute(
        self,
        request: IngestionPipelineRequest,
    ) -> IngestionPipelineResponse:
        """
        Execute ingestion.
        """

        loaded = self.ingestion.ingest(
            IngestionRequest(
                document_id=request.document_id,
                storage_key=request.storage_key,
                absolute_path=Path(
                    request.absolute_path,
                ),
            )
        )

        chunks = self.chunker.chunk(
            loaded.content,
        )

        embeddings = self.embedding.embed(
            chunks,
        )

        records: list[VectorRecord] = []

        for embedded in embeddings:
            records.append(
                VectorRecord(
                    document_id=request.document_id,
                    chunk_index=embedded.chunk_index,
                    text=embedded.text,
                    embedding=embedded.embedding,
                )
            )

        self.vector_store.upsert(
            records,
        )

        return IngestionPipelineResponse(
            document_id=request.document_id,
            chunks=len(chunks),
            vectors=len(records),
        )
