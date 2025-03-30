from fastapi import FastAPI

from internal.download.api.v1.routers import router as download_router
from internal.healthcheck.api.v1.routers import router as healthcheck_router


def init_routers(
        app: FastAPI
) -> None:
    app.include_router(download_router)
    app.include_router(healthcheck_router)
