"""
PDF loader.
"""

from pathlib import Path

from ingestion.loaders.base import DocumentLoader
from ingestion.schemas import LoadedDocument
from pypdf import PdfReader


class PdfDocumentLoader(DocumentLoader):
    """
    PDF loader.
    """

    def load(
        self,
        path: Path,
    ) -> LoadedDocument:
        reader = PdfReader(path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return LoadedDocument(
            content=text,
            metadata={
                "pages": str(len(reader.pages)),
            },
        )
