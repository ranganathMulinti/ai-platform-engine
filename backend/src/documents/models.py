"""
Document ORM model.
"""

from __future__ import annotations

from core.models.base import BaseModel
from documents.constants import (
    DEFAULT_CHUNK_COUNT,
    MAX_DESCRIPTION_LENGTH,
    MAX_FILENAME_LENGTH,
    MAX_TITLE_LENGTH,
)
from documents.enums import (
    DocumentStatus,
    StorageProvider,
)
from sqlalchemy import Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Document(BaseModel):
    """
    Document entity.
    """

    __tablename__ = "documents"

    owner_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    title: Mapped[str] = mapped_column(
        String(MAX_TITLE_LENGTH),
    )

    description: Mapped[str | None] = mapped_column(
        String(MAX_DESCRIPTION_LENGTH),
        nullable=True,
    )

    filename: Mapped[str] = mapped_column(
        String(MAX_FILENAME_LENGTH),
    )

    original_filename: Mapped[str] = mapped_column(
        String(MAX_FILENAME_LENGTH),
    )

    mime_type: Mapped[str] = mapped_column(
        String(255),
    )

    file_size: Mapped[int] = mapped_column(
        Integer,
    )

    checksum: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        index=True,
    )

    storage_provider: Mapped[StorageProvider] = mapped_column(
        Enum(StorageProvider),
        default=StorageProvider.LOCAL,
    )

    storage_key: Mapped[str] = mapped_column(
        String(1024),
    )

    status: Mapped[DocumentStatus] = mapped_column(
        Enum(DocumentStatus),
        default=DocumentStatus.UPLOADED,
        index=True,
    )

    chunk_count: Mapped[int] = mapped_column(
        Integer,
        default=DEFAULT_CHUNK_COUNT,
    )

    embedding_model: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    vector_collection: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
