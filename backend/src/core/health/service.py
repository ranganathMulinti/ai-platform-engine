from core.health.schemas import HealthResponse


class HealthService:
    """
    Service class for handling health checks.
    """

    def get_liveness(self) -> HealthResponse:
        """
        Get the liveness status of the application.

        Returns:
            HealthResponse: The liveness response.
        """
        return HealthResponse(status="alive")

    def get_readiness(self) -> HealthResponse:
        """
        Get the readiness status of the application.

        Returns:
            HealthResponse: The readiness response.
        """
        return HealthResponse(status="ready")
