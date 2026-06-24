from core.exceptions import DatabaseConnectionError, DatabaseError, PlatformError, TransactionError


def test_database_error_inheritance():
    """Test that DatabaseError is a subclass of PlatformError."""
    assert issubclass(DatabaseError, PlatformError)


def test_database_connection_error_message():
    """Test that DatabaseConnectionError stores the message."""
    error = DatabaseConnectionError("Connection failed")
    assert error.message == "Connection failed"


def test_transaction_error_message() -> None:
    """Test that TransactionError stores the message."""
    error = TransactionError("Transaction failed")
    assert error.message == "Transaction failed"
    assert str(error) == "Transaction failed"


def test_string_representation():
    """Test that exceptions return the message when converted to string."""
    error = DatabaseConnectionError("Connection failed")
    assert str(error) == "Connection failed"
