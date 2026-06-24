from core.exceptions import (
    APIError,
    ForbiddenError,
    PlatformError,
    ResourceNotFoundError,
    UnauthorizedError,
)


def test_api_error_inheritance():
    """Test that APIError is a subclass of PlatformError."""
    assert issubclass(APIError, PlatformError)


def test_resource_not_found_message():
    """Test that ResourceNotFoundError stores the message."""
    error = ResourceNotFoundError("Resource not found")
    assert error.message == "Resource not found"


def test_unauthorized_error_message():
    """Test that UnauthorizedError stores the message."""
    error = UnauthorizedError("Authentication required")
    assert error.message == "Authentication required"


def test_forbidden_error_message():
    """Test that ForbiddenError stores the message."""
    error = ForbiddenError("Permission denied")
    assert error.message == "Permission denied"


def test_string_representation():
    """Test that exceptions return the message when converted to string."""
    error = ResourceNotFoundError("Resource not found")
    assert str(error) == "Resource not found"
