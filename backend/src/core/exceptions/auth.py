"""
Authentication exceptions.
"""

from core.exceptions.base import AppException
from fastapi import status


class AuthenticationException(AppException):
    status_code = status.HTTP_401_UNAUTHORIZED

    detail = "Authentication failed."


class InvalidCredentialsException(AuthenticationException):
    detail = "Invalid credentials."


class UserAlreadyExistsException(AppException):
    status_code = status.HTTP_409_CONFLICT

    detail = "User already exists."


class InvalidTokenException(AuthenticationException):
    detail = "Invalid token."


class InactiveUserException(AuthenticationException):
    detail = "Inactive user."
