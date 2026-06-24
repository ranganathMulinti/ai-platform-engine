import logging


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance with the given name.

    Args:
        name: The name of the logger.

    Returns:
        A logger instance.
    """
    return logging.getLogger(name)
