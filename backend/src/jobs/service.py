"""
Job service.
"""

from collections.abc import Callable

from jobs.base import JobQueue
from jobs.schemas import Job


class JobService:
    """
    Job service.
    """

    def __init__(
        self,
        provider: JobQueue,
    ) -> None:
        self.provider = provider

    def submit(
        self,
        name: str,
        task: Callable[[], None],
    ) -> Job:
        return self.provider.submit(
            name,
            task,
        )
