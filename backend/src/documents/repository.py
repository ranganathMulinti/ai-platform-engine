"""
Document repository.
"""

from core.repositories.base import BaseRepository
from documents.enums import DocumentStatus
from documents.models import Document
from sqlalchemy import select
from sqlalchemy.orm import Session


class DocumentRepository(BaseRepository[Document]):
    """
    Repository for Document entities.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:
        super().__init__(
            session=session,
            model=Document,
        )

    def get_by_checksum(
        self,
        checksum: str,
    ) -> Document | None:
        """
        Retrieve a document by checksum.
        """

        stmt = select(Document).where(Document.checksum == checksum)

        return self.session.scalar(stmt)

    def get_by_status(
        self,
        status: DocumentStatus,
    ) -> list[Document]:
        """
        Retrieve documents by processing status.
        """

        stmt = select(Document).where(Document.status == status)

        return list(self.session.scalars(stmt))
