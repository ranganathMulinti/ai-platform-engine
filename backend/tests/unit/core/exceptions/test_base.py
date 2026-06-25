from core.exceptions import AppException


def test_app_exception_defaults() -> None:
    exc = AppException()

    assert exc.status_code == 500
    assert exc.detail == "Application Error"


def test_app_exception_custom_detail() -> None:
    exc = AppException("Custom message")

    assert exc.detail == "Custom message"
