"""
Pipeline schemas.
"""

from pydantic import BaseModel


class IngestionPipelineRequest(BaseModel):
    """
    Pipeline request.
    """

    document_id: int

    storage_key: str

    absolute_path: str


class IngestionPipelineResponse(BaseModel):
    """
    Pipeline response.
    """

    document_id: int

    chunks: int

    vectors: int
