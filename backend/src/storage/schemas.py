"""
Storage schemas.
"""

from pydantic import BaseModel


class StoredFile(BaseModel):
    """
    Represents a file successfully stored by a storage provider.
    """

    filename: str

    original_filename: str

    mime_type: str

    file_size: int

    checksum: str

    key: str
