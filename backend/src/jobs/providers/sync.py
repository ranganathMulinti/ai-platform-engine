"""
Synchronous job queue.
"""

from collections.abc import Callable
from uuid import uuid4

from jobs.base import JobQueue
from jobs.schemas import (
    Job,
    JobStatus,
)


class SyncJobQueue(JobQueue):
    """
    Executes jobs immediately.
    """

    def submit(
        self,
        name: str,
        task: Callable[[], None],
    ) -> Job:
        job = Job(
            id=str(uuid4()),
            name=name,
            status=JobStatus.RUNNING,
        )

        try:
            task()

            job.status = JobStatus.COMPLETED

        except Exception:
            job.status = JobStatus.FAILED

            raise

        return job
