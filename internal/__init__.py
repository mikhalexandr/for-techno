from fastapi import FastAPI

from internal.healthcheck.api.v1.routers import router as healthcheck_router
from internal.superadmin.api.v1.routers import router as superadmin_router
from internal.user.api.v1.routers import router as user_router


def init_routers(
        app: FastAPI
) -> None:
    app.include_router(healthcheck_router)
    app.include_router(superadmin_router)
    app.include_router(user_router)
