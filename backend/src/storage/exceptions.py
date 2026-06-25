"""
Storage exceptions.
"""

from core.exceptions.base import AppException
from fastapi import status


class StorageException(AppException):
    """
    Base storage exception.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    detail = "Storage operation failed."


class FileNotFoundException(StorageException):
    """
    File not found.
    """

    status_code = status.HTTP_404_NOT_FOUND

    detail = "Stored file not found."


class FileAlreadyExistsException(StorageException):
    """
    File already exists.
    """

    status_code = status.HTTP_409_CONFLICT

    detail = "File already exists."
