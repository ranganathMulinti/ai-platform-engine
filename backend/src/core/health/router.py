from core.dependencies import get_health_service  # Added this line
from core.health.schemas import HealthResponse
from core.health.service import HealthService
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/health")


@router.get("/live", response_model=HealthResponse)
async def live(health_service: HealthService = Depends(get_health_service)) -> HealthResponse:
    """
    Endpoint to check the liveness of the application.

    Returns:
        HealthResponse: The liveness response.
    """
    return health_service.get_liveness()


@router.get("/ready", response_model=HealthResponse)
async def ready(health_service: HealthService = Depends(get_health_service)) -> HealthResponse:
    """
    Endpoint to check the readiness of the application.

    Returns:
        HealthResponse: The readiness response.
    """
    return health_service.get_readiness()
