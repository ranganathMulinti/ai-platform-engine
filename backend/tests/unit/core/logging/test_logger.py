from core.logging import get_logger


def test_logger_singleton():
    logger1 = get_logger("test")
    logger2 = get_logger("test")
    assert logger1 is logger2
