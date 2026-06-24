from abc import ABC, abstractmethod


class UnitOfWork[T](ABC):
    """
    Abstract base class for a unit of work.

    Attributes:
        session (Session): The database session.
    """

    @abstractmethod
    def commit(self) -> None:
        """
        Commit the current transaction.
        """
        pass

    @abstractmethod
    def rollback(self) -> None:
        """
        Rollback the current transaction.
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """
        Close the session.
        """
        pass
