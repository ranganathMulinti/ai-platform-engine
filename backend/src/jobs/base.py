"""
Job queue interface.
"""

from abc import ABC, abstractmethod
from collections.abc import Callable

from jobs.schemas import Job


class JobQueue(ABC):
    """
    Base job queue.
    """

    @abstractmethod
    def submit(
        self,
        name: str,
        task: Callable[[], None],
    ) -> Job:
        """
        Submit a job.
        """
