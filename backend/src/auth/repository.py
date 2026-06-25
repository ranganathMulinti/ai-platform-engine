"""
Authentication repository.
"""

from auth.models import User
from core.repositories.base import BaseRepository
from sqlalchemy import select
from sqlalchemy.orm import Session


class UserRepository(BaseRepository[User]):
    """
    Repository for User entities.
    """

    def __init__(self, session: Session) -> None:
        super().__init__(session, User)

    def get_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by email.

        Args:
            email: User email.

        Returns:
            User if found, otherwise None.
        """
        stmt = select(User).where(User.email == email)

        return self.session.scalar(stmt)
