"""
Tool exceptions.
"""

from core.exceptions.base import AppException
from fastapi import status


class ToolException(AppException):
    """
    Base tool exception.
    """

    status_code = status.HTTP_400_BAD_REQUEST

    detail = "Tool execution failed."


class ToolNotFoundException(ToolException):
    """
    Tool not found.
    """

    status_code = status.HTTP_404_NOT_FOUND

    detail = "Tool not found."
