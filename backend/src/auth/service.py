"""
Authentication service.
"""

from auth.constants import ACCESS_TOKEN_TYPE
from auth.exceptions import (
    InvalidCredentialsException,
    UserAlreadyExistsException,
)
from auth.models import User
from auth.schemas import (
    TokenResponse,
    UserCreate,
    UserLogin,
    UserResponse,
)
from auth.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from auth.unit_of_work import AuthUnitOfWork


class AuthService:
    """
    Authentication business logic.
    """

    def __init__(
        self,
        uow: AuthUnitOfWork,
    ) -> None:
        self.uow = uow

    def register(
        self,
        request: UserCreate,
    ) -> UserResponse:
        """
        Register a new user.
        """

        existing_user = self.uow.user_repository.get_by_email(
            request.email,
        )

        if existing_user is not None:
            raise UserAlreadyExistsException("User already exists.")

        user = User(
            email=request.email,
            hashed_password=hash_password(
                request.password,
            ),
            full_name=request.full_name,
        )

        self.uow.user_repository.add(user)
        self.uow.commit()
        self.uow.user_repository.refresh(user)

        return UserResponse.model_validate(user)

    def login(
        self,
        request: UserLogin,
    ) -> TokenResponse:
        """
        Authenticate a user.
        """

        user = self.uow.user_repository.get_by_email(
            request.email,
        )

        if user is None:
            raise InvalidCredentialsException("Invalid credentials.")

        if not verify_password(
            request.password,
            user.hashed_password,
        ):
            raise InvalidCredentialsException("Invalid credentials.")

        access_token = create_access_token(
            subject=user.email,
        )

        return TokenResponse(
            access_token=access_token,
            token_type=ACCESS_TOKEN_TYPE,
        )
