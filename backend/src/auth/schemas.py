"""
Authentication request and response schemas.
"""

from auth.constants import FULL_NAME_MAX_LENGTH
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    """User registration payload."""

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )

    full_name: str | None = Field(
        default=None,
        max_length=FULL_NAME_MAX_LENGTH,
    )


class UserLogin(BaseModel):
    """Login payload."""

    email: EmailStr

    password: str


class UserResponse(BaseModel):
    """User response DTO."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    full_name: str | None
    is_active: bool
    is_superuser: bool


class TokenResponse(BaseModel):
    """JWT token response."""

    access_token: str
    token_type: str
