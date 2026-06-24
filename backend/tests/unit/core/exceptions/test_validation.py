from core.exceptions import PlatformError, ValidationError


def test_validation_error_inheritance():
    """Test that ValidationError is a subclass of PlatformError."""
    assert issubclass(ValidationError, PlatformError)


def test_validation_error_message():
    """Test that ValidationError stores the message."""
    error = ValidationError("Validation failed")
    assert error.message == "Validation failed"


def test_string_representation():
    """Test that exceptions return the message when converted to string."""
    error = ValidationError("Validation failed")
    assert str(error) == "Validation failed"
