"""
Authentication dependencies.
"""

from auth.models import User
from auth.repository import UserRepository
from auth.security import decode_access_token
from core.database.session import get_db
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)


def get_user_repository(
    db: Session = Depends(get_db),
) -> UserRepository:
    """
    Dependency that returns a UserRepository.
    """

    return UserRepository(db)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    repository: UserRepository = Depends(
        get_user_repository,
    ),
) -> User:
    """
    Return the authenticated user.
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = decode_access_token(token)

        email = payload.get("sub")

        if not isinstance(email, str):
            raise credentials_exception

    except InvalidTokenError as err:
        raise credentials_exception from err

    user = repository.get_by_email(email)

    if user is None:
        raise credentials_exception

    return user
