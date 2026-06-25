"""
Authentication Unit of Work.
"""

from auth.repository import UserRepository
from core.unit_of_work.sqlalchemy import SqlAlchemyUnitOfWork


class AuthUnitOfWork(SqlAlchemyUnitOfWork):
    """
    Unit of Work for authentication.
    """

    def __init__(self) -> None:
        super().__init__()

        self.user_repository = UserRepository(
            self.session,
        )
