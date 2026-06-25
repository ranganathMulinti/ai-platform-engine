"""
Authentication ORM models.
"""

from auth.constants import (
    EMAIL_MAX_LENGTH,
    FULL_NAME_MAX_LENGTH,
    PASSWORD_HASH_MAX_LENGTH,
)
from core.models.base import BaseModel
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column


class User(BaseModel):
    """
    Application user.
    """

    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        String(EMAIL_MAX_LENGTH),
        unique=True,
        nullable=False,
        index=True,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(PASSWORD_HASH_MAX_LENGTH),
        nullable=False,
    )

    full_name: Mapped[str | None] = mapped_column(
        String(FULL_NAME_MAX_LENGTH),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    def __repr__(self) -> str:
        """Return object representation."""
        return f"User(id={self.id}, email='{self.email}', is_active={self.is_active})"
