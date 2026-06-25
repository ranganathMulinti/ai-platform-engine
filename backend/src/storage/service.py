"""
Storage service.
"""

from fastapi import UploadFile
from storage.base import StorageProvider
from storage.schemas import StoredFile


class StorageService:
    """
    Application storage service.
    """

    def __init__(
        self,
        provider: StorageProvider,
    ) -> None:
        self.provider = provider

    def store(
        self,
        file: UploadFile,
    ) -> StoredFile:
        return self.provider.store(
            file,
        )

    def delete(
        self,
        key: str,
    ) -> None:
        self.provider.delete(
            key,
        )

    def exists(
        self,
        key: str,
    ) -> bool:
        return self.provider.exists(
            key,
        )
