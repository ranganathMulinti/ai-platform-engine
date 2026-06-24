from .base import PlatformError


class DatabaseError(PlatformError):
    """Base class for database-related exceptions."""


class DatabaseConnectionError(DatabaseError):
    """Exception raised when a database connection fails."""


class TransactionError(DatabaseError):
    """Exception raised when a database transaction fails."""
