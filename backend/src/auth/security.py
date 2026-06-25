"""
Authentication security utilities.
"""

from datetime import UTC, datetime, timedelta
from typing import Any

import jwt
from core.dependencies import get_settings
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

settings = get_settings()


def hash_password(password: str) -> str:
    """
    Hash a plain text password.
    """
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    Verify a password against its hash.
    """
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(
    subject: str,
    expires_delta: timedelta | None = None,
) -> str:
    """
    Create a signed JWT access token.
    """

    expire = datetime.now(UTC) + (
        expires_delta
        or timedelta(
            minutes=settings.access_token_expire_minutes,
        )
    )

    payload: dict[str, Any] = {
        "sub": subject,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm,
    )


def decode_access_token(
    token: str,
) -> dict[str, object]:
    """
    Decode a JWT access token.
    """

    return jwt.decode(
        token,
        settings.secret_key,
        algorithms=[settings.algorithm],
    )
