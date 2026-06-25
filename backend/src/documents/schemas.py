"""
Document schemas.
"""

from documents.constants import (
    MAX_DESCRIPTION_LENGTH,
    MAX_TITLE_LENGTH,
)
from documents.enums import (
    DocumentStatus,
    StorageProvider,
)
from pydantic import BaseModel, ConfigDict, Field


class DocumentCreate(BaseModel):
    """
    Create document request.
    """

    title: str = Field(
        max_length=MAX_TITLE_LENGTH,
    )

    description: str | None = Field(
        default=None,
        max_length=MAX_DESCRIPTION_LENGTH,
    )


class DocumentResponse(BaseModel):
    """
    Document response DTO.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    title: str

    description: str | None

    filename: str

    original_filename: str

    mime_type: str

    file_size: int

    checksum: str

    storage_provider: StorageProvider

    status: DocumentStatus

    chunk_count: int
