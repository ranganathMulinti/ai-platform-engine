from types import TracebackType
from unittest.mock import MagicMock

from core.unit_of_work.base import UnitOfWork
from sqlalchemy.orm import Session


class ConcreteUnitOfWork(UnitOfWork):
    def __init__(self, session: Session):
        self.session = session

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if exc_type:
            self.rollback()
        self.close()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()


def test_commit() -> None:
    session = MagicMock(spec=Session)

    uow = ConcreteUnitOfWork(session)

    uow.commit()

    session.commit.assert_called_once()


def test_rollback() -> None:
    session = MagicMock(spec=Session)

    uow = ConcreteUnitOfWork(session)

    uow.rollback()

    session.rollback.assert_called_once()


def test_close() -> None:
    session = MagicMock(spec=Session)

    uow = ConcreteUnitOfWork(session)

    uow.close()

    session.close.assert_called_once()
