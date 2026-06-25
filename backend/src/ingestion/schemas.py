"""
Ingestion schemas.
"""

from pathlib import Path

from pydantic import BaseModel


class IngestionRequest(BaseModel):
    """
    Document ingestion request.
    """

    document_id: int

    storage_key: str

    absolute_path: Path


class LoadedDocument(BaseModel):
    """
    Document loaded from storage.
    """

    content: str

    metadata: dict[str, str]
