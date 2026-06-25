"""
Document dependencies.
"""

from pathlib import Path

from documents.service import DocumentService
from documents.unit_of_work import DocumentUnitOfWork
from fastapi import Depends
from storage.providers.local import LocalStorageProvider
from storage.service import StorageService


def get_document_uow() -> DocumentUnitOfWork:
    """
    Document Unit of Work dependency.
    """

    return DocumentUnitOfWork()


def get_storage_service() -> StorageService:
    """
    Storage service dependency.
    """

    provider = LocalStorageProvider(
        Path("storage"),
    )

    return StorageService(provider)


def get_document_service(
    uow: DocumentUnitOfWork = Depends(
        get_document_uow,
    ),
) -> DocumentService:
    """
    Document service dependency.
    """

    return DocumentService(uow)
