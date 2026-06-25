"""
Document enums.
"""

from enum import StrEnum


class DocumentStatus(StrEnum):
    """
    Processing status of a document.
    """

    UPLOADED = "UPLOADED"
    PROCESSING = "PROCESSING"
    EMBEDDED = "EMBEDDED"
    READY = "READY"
    FAILED = "FAILED"
    DELETED = "DELETED"


class StorageProvider(StrEnum):
    """
    Supported storage providers.
    """

    LOCAL = "LOCAL"
    AWS_S3 = "AWS_S3"
