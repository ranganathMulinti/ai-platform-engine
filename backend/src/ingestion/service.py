"""
Ingestion service.
"""

from pathlib import Path

from ingestion.loaders.pdf import PdfDocumentLoader
from ingestion.schemas import (
    IngestionRequest,
    LoadedDocument,
)


class IngestionService:
    """
    Document ingestion service.
    """

    def __init__(self) -> None:
        self.loader = PdfDocumentLoader()

    def ingest(
        self,
        request: IngestionRequest,
    ) -> LoadedDocument:
        """
        Load a document.
        """

        return self.loader.load(
            Path(request.absolute_path),
        )
