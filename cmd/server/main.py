from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infra.logger import init_logger, logger
from infra.keycloak_.access import init_keycloak_client, close_keycloak_client
from infra.llama3.access import init_llama3_client, close_llama3_client
from infra.postgres.access import init_postgres_client, close_postgres_client
from infra.settings import settings
from internal import init_routers


@asynccontextmanager
async def lifespan(
        _app: FastAPI
) -> AsyncGenerator:
    init_logger()
    await init_keycloak_client()
    await init_llama3_client()
    await init_postgres_client()
    logger.info("All resources have been successfully initialized")
    yield
    await close_keycloak_client()
    await close_llama3_client()
    await close_postgres_client()
    logger.info("All resources have been successfully closed")


def init_app() -> FastAPI:
    _app = FastAPI(
        title="tetris",
        version="1.0.0",
        license_info={
            "name": "MIT License",
            "url": "https://opensource.org/licenses/MIT",
        },
        openapi_url="/api/openapi.json",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        lifespan=lifespan,
    )
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    init_routers(_app)
    return _app


app = init_app()

if __name__ == "__main__":
    host, port = settings.server_address.split(":")
    uvicorn.run(
        app,
        host=host,
        port=int(port)
    )
