"""
Authentication API router.
"""

from auth.schemas import (
    TokenResponse,
    UserCreate,
    UserLogin,
    UserResponse,
)
from auth.service import AuthService
from auth.unit_of_work import AuthUnitOfWork
from fastapi import (
    APIRouter,
    Depends,
    status,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


def get_auth_uow() -> AuthUnitOfWork:
    """
    Authentication Unit of Work dependency.
    """
    return AuthUnitOfWork()


def get_auth_service(
    uow: AuthUnitOfWork = Depends(get_auth_uow),
) -> AuthService:
    """
    Authentication service dependency.
    """
    return AuthService(uow)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: UserCreate,
    service: AuthService = Depends(
        get_auth_service,
    ),
) -> UserResponse:
    """
    Register a new user.
    """
    return service.register(request)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: UserLogin,
    service: AuthService = Depends(
        get_auth_service,
    ),
) -> TokenResponse:
    """
    Authenticate a user.
    """
    return service.login(request)
