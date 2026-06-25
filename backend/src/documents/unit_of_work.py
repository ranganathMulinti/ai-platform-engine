"""
Document Unit of Work.
"""

from core.unit_of_work.sqlalchemy import SqlAlchemyUnitOfWork
from documents.repository import DocumentRepository


class DocumentUnitOfWork(SqlAlchemyUnitOfWork):
    """
    Unit of Work for document operations.
    """

    def __init__(self) -> None:
        super().__init__()

        self.document_repository = DocumentRepository(
            self.session,
        )
