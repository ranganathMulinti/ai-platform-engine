from pydantic import BaseModel


class HealthResponse(BaseModel):
    """
    Pydantic model for health response.

    Attributes:
        status (str): The status of the application.
    """

    status: str
