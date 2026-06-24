import json
import logging
from datetime import datetime


class JsonFormatter(logging.Formatter):
    """Format log records as JSON with UTC timestamp.

    Output format:
        {
            "timestamp": "2024-05-23T12:34:56.789Z",
            "level": "INFO",
            "logger": "my_logger",
            "message": "Hello, world!"
        }
    """

    def format(self, record: logging.LogRecord) -> str:
        timestamp = datetime.utcnow().isoformat() + "Z"
        record_dict = {
            "timestamp": timestamp,
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        return json.dumps(record_dict)
