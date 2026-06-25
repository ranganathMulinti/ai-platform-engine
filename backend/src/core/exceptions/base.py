"""
Base application exceptions.
"""


class AppException(Exception):
    """
    Base class for all application exceptions.
    """

    status_code: int = 500

    detail: str = "Application Error"

    def __init__(
        self,
        detail: str | None = None,
    ) -> None:
        super().__init__(detail or self.detail)

        if detail:
            self.detail = detail
