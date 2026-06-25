"""
Storage provider interface.
"""

from abc import ABC, abstractmethod

from fastapi import UploadFile
from storage.schemas import StoredFile


class StorageProvider(ABC):
    """
    Abstract storage provider.
    """

    @abstractmethod
    def store(
        self,
        file: UploadFile,
    ) -> StoredFile:
        """
        Store a file.
        """

    @abstractmethod
    def delete(
        self,
        key: str,
    ) -> None:
        """
        Delete a stored file.
        """

    @abstractmethod
    def exists(
        self,
        key: str,
    ) -> bool:
        """
        Determine whether a file exists.
        """
