class PlatformError(Exception):
    """Base class for all platform exceptions.

    This class serves as the foundation for all exceptions in the AI Platform Engine.
    """

    def __init__(self, message: str):
        super().__init__()
        self.message = message

    def __str__(self) -> str:
        return self.message
