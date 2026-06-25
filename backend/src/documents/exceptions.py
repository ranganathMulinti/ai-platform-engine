"""
Document exceptions.
"""

from core.exceptions.base import AppException
from fastapi import status


class DocumentException(AppException):
    """
    Base document exception.
    """

    status_code = status.HTTP_400_BAD_REQUEST

    detail = "Document error."


class DocumentNotFoundException(DocumentException):
    """
    Document not found.
    """

    status_code = status.HTTP_404_NOT_FOUND

    detail = "Document not found."


class DuplicateDocumentException(DocumentException):
    """
    Duplicate document.
    """

    status_code = status.HTTP_409_CONFLICT

    detail = "Document already exists."


class InvalidDocumentStateException(DocumentException):
    """
    Invalid state transition.
    """

    status_code = status.HTTP_409_CONFLICT

    detail = "Invalid document state."
