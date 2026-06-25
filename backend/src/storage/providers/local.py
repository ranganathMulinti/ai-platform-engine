"""
Local filesystem storage provider.
"""

from hashlib import sha256
from pathlib import Path
from shutil import copyfileobj

from fastapi import UploadFile
from storage.base import StorageProvider
from storage.constants import (
    DEFAULT_DOCUMENT_DIRECTORY,
    SHA256_CHUNK_SIZE,
)
from storage.exceptions import (
    FileAlreadyExistsException,
    FileNotFoundException,
)
from storage.schemas import StoredFile


class LocalStorageProvider(StorageProvider):
    """
    Local filesystem implementation.
    """

    def __init__(
        self,
        root_directory: Path,
    ) -> None:
        self.root_directory = root_directory

        self.root_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def store(
        self,
        file: UploadFile,
    ) -> StoredFile:
        digest = sha256()

        while chunk := file.file.read(
            SHA256_CHUNK_SIZE,
        ):
            digest.update(chunk)

        checksum = digest.hexdigest()

        file.file.seek(0)

        key = f"{DEFAULT_DOCUMENT_DIRECTORY}/{checksum}_{file.filename}"

        destination = self.root_directory / key

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if destination.exists():
            raise FileAlreadyExistsException()

        with destination.open("wb") as output:
            copyfileobj(
                file.file,
                output,
            )

        return StoredFile(
            filename=destination.name,
            original_filename=file.filename or destination.name,
            mime_type=file.content_type or "application/octet-stream",
            file_size=destination.stat().st_size,
            checksum=checksum,
            key=key,
        )

    def delete(
        self,
        key: str,
    ) -> None:
        path = self.root_directory / key

        if not path.exists():
            raise FileNotFoundException()

        path.unlink()

    def exists(
        self,
        key: str,
    ) -> bool:
        return (self.root_directory / key).exists()
