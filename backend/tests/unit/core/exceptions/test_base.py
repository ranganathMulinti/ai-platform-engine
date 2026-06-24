from core.exceptions import PlatformError


def test_platform_error_inheritance():
    """Test that PlatformError is a subclass of Exception."""
    assert issubclass(PlatformError, Exception)


def test_platform_error_message():
    """Test that PlatformError stores the message."""
    error = PlatformError("Test message")
    assert error.message == "Test message"


def test_platform_error_string_representation():
    """Test that PlatformError returns the message when converted to string."""
    error = PlatformError("Test message")
    assert str(error) == "Test message"
