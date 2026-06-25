"""
Job schemas.
"""

from enum import StrEnum

from pydantic import BaseModel


class JobStatus(StrEnum):
    """
    Job status.
    """

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Job(BaseModel):
    """
    Background job.
    """

    id: str

    name: str

    status: JobStatus
