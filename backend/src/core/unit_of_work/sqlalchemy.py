"""
SQLAlchemy implementation of Unit of Work.
"""

from types import TracebackType

from core.database.session import SessionLocal
from core.unit_of_work.base import UnitOfWork
from sqlalchemy.orm import Session


class SqlAlchemyUnitOfWork(UnitOfWork):
    """
    SQLAlchemy implementation of the Unit of Work pattern.
    """

    def __init__(self) -> None:
        self.session: Session = SessionLocal()

    def __enter__(self) -> "SqlAlchemyUnitOfWork":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        _exc_value: BaseException | None,
        _traceback: TracebackType | None,
    ) -> None:
        """
        Exit the context manager.
        Rolls back the transaction if an exception occurred,
        then always closes the session.
        """

        if exc_type is not None:
            self.rollback()
        self.close()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()
