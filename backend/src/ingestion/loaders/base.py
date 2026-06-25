"""
Base document loader.
"""

from abc import ABC, abstractmethod
from pathlib import Path

from ingestion.schemas import LoadedDocument


class DocumentLoader(ABC):
    """
    Base loader.
    """

    @abstractmethod
    def load(
        self,
        path: Path,
    ) -> LoadedDocument:
        """
        Load a document.
        """
