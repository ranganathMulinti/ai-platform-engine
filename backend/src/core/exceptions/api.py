from .base import PlatformError


class APIError(PlatformError):
    """Base class for API-related exceptions."""


class ResourceNotFoundError(APIError):
    """Exception raised when a resource is not found."""


class UnauthorizedError(APIError):
    """Exception raised when authentication is required but not provided."""


class ForbiddenError(APIError):
    """Exception raised when the user does not have permission to access the resource."""
