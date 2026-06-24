import json
import logging

from core.logging import JsonFormatter


def test_json_formatter() -> None:
    formatter = JsonFormatter()
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="Hello, world!",
        args=(),
        exc_info=None,
    )

    formatted = formatter.format(record)

    data = json.loads(formatted)

    assert data["level"] == "INFO"
    assert data["logger"] == "test"
    assert data["message"] == "Hello, world!"
    assert "timestamp" in data
