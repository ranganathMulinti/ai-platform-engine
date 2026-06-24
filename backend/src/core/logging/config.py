import logging

from core.config import Environment, Settings

from .formatter import JsonFormatter


def configure_logging() -> None:
    """Configure logging based on environment settings.

    This function sets up the logging configuration for the application.
    """
    settings = Settings()
    log_level = settings.log_level

    logger = logging.getLogger()
    if logger.handlers:
        return

    # Configure console handler
    console_handler = logging.StreamHandler()

    # Set log level
    logger.setLevel(log_level)

    # Configure formatter based on environment
    if settings.environment == Environment.production:
        console_handler.setFormatter(JsonFormatter())
    else:
        console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

    # Add handler
    logger.addHandler(console_handler)
