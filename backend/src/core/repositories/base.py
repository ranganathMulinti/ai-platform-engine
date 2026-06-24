from core.models.base import BaseModel
from sqlalchemy import exists, select
from sqlalchemy.orm import Session


class BaseRepository[T: BaseModel]:
    """
    Base repository class with common CRUD operations.

    Attributes:
        model (Type[T]): The model class associated with the repository.
    """

    def __init__(
        self,
        session: Session,
        model: type[T],
    ) -> None:
        self.session = session
        self.model = model

    def get(self, entity_id: int) -> T | None:
        """
        Get a record by its ID.

        Args:
            entity_id (int): The ID of the record to retrieve.

        Returns:
            Optional[T]: The retrieved record or None if not found.
        """
        return self.session.get(self.model, entity_id)

    def list(self) -> list[T]:
        """Return all entities."""

        stmt = select(self.model)

        return list(self.session.scalars(stmt))

    def add(self, obj: T) -> None:
        """
        Add a new record.

        Args:
            obj (T): The record to add.
        """
        self.session.add(obj)

    def delete(self, obj: T) -> None:
        """
        Delete a record.

        Args:
            obj (T): The record to delete.
        """
        self.session.delete(obj)

    def exists(self, entity_id: int) -> bool:
        """
        Check if a record with the given ID exists.

        Args:
            id (int): The ID of the record to check.

        Returns:
            bool: True if the record exists, False otherwise.
        """
        stmt = select(exists().where(self.model.id == entity_id))
        return bool(self.session.scalar(stmt))

    def flush(self) -> None:
        """Flush pending changes to the database."""
        self.session.flush()

    def refresh(self, obj: T) -> None:
        """Refresh an entity from the database."""
        self.session.refresh(obj)
