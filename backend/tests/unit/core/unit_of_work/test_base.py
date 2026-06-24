from unittest.mock import MagicMock

from core.unit_of_work.base import UnitOfWork
from sqlalchemy.orm import Session


class ConcreteUnitOfWork(UnitOfWork):
    """Concrete implementation used for unit testing."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()


def test_commit() -> None:
    """Test commit delegates to SQLAlchemy session."""
    session = MagicMock(spec=Session)

    uow = ConcreteUnitOfWork(session)

    uow.commit()

    session.commit.assert_called_once()


def test_rollback() -> None:
    """Test rollback delegates to SQLAlchemy session."""
    session = MagicMock(spec=Session)

    uow = ConcreteUnitOfWork(session)

    uow.rollback()

    session.rollback.assert_called_once()


def test_close() -> None:
    """Test close delegates to SQLAlchemy session."""
    session = MagicMock(spec=Session)

    uow = ConcreteUnitOfWork(session)

    uow.close()

    session.close.assert_called_once()
