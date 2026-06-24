from unittest.mock import MagicMock

from core.models.base import BaseModel
from core.repositories.base import BaseRepository
from sqlalchemy import String
from sqlalchemy.orm import Mapped, Session, mapped_column


class SampleModel(BaseModel):
    """Sample model used for repository unit tests."""

    __tablename__ = "sample_models"

    name: Mapped[str] = mapped_column(String(255))


def test_repository_initialization() -> None:
    """Test repository initialization."""
    session = MagicMock(spec=Session)

    repository = BaseRepository(session, SampleModel)

    assert repository.session is session
    assert repository.model is SampleModel


def test_add() -> None:
    """Test add delegates to SQLAlchemy session."""
    session = MagicMock(spec=Session)
    repository = BaseRepository(session, SampleModel)

    entity = SampleModel(name="Test")

    repository.add(entity)

    session.add.assert_called_once_with(entity)


def test_delete() -> None:
    """Test delete delegates to SQLAlchemy session."""
    session = MagicMock(spec=Session)
    repository = BaseRepository(session, SampleModel)

    entity = SampleModel(name="Test")

    repository.delete(entity)

    session.delete.assert_called_once_with(entity)


def test_flush() -> None:
    """Test flush delegates to SQLAlchemy session."""
    session = MagicMock(spec=Session)
    repository = BaseRepository(session, SampleModel)

    repository.flush()

    session.flush.assert_called_once()


def test_refresh() -> None:
    """Test refresh delegates to SQLAlchemy session."""
    session = MagicMock(spec=Session)
    repository = BaseRepository(session, SampleModel)

    entity = SampleModel(name="Test")

    repository.refresh(entity)

    session.refresh.assert_called_once_with(entity)


def test_get() -> None:
    """Test get delegates to SQLAlchemy session."""
    session = MagicMock(spec=Session)
    repository = BaseRepository(session, SampleModel)

    entity = SampleModel(name="Test")
    session.get.return_value = entity

    result = repository.get(1)

    session.get.assert_called_once_with(SampleModel, 1)
    assert result is entity


def test_list() -> None:
    """Test list delegates to SQLAlchemy session."""
    session = MagicMock(spec=Session)
    repository = BaseRepository(session, SampleModel)

    entities = [SampleModel(name="One"), SampleModel(name="Two")]

    session.scalars.return_value = entities

    result = repository.list()

    session.scalars.assert_called_once()
    assert result == entities


def test_exists() -> None:
    """Test exists delegates to SQLAlchemy session."""
    session = MagicMock(spec=Session)
    repository = BaseRepository(session, SampleModel)

    session.scalar.return_value = True

    assert repository.exists(1) is True

    session.scalar.assert_called_once()
