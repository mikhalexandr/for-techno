import time
from datetime import datetime

from fastapi import APIRouter

from internal.healthcheck.schemes.healthcheck import HealthcheckRootRs, HealthcheckPingRs

router = APIRouter(
    tags=["Healthcheck"]
)


@router.get(
    "/",
    status_code=200,
    response_model=HealthcheckRootRs,
    include_in_schema=False,
)
async def root() -> HealthcheckRootRs:
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return HealthcheckRootRs(
        status="OK",
        current_time=current_time
    )


@router.get(
    "/api/ping",
    status_code=200,
    response_model=HealthcheckPingRs
)
async def ping() -> HealthcheckPingRs:
    start_time = time.time()
    response = HealthcheckPingRs(
        status="pong",
        response_time=0.0
    )
    end_time = time.time()
    response.response_time = end_time - start_time
    return response
