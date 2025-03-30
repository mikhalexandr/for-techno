from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.logger import init_logger, logger
from core.minio.access import init_minio_client, close_minio_client
from core.postgres.access import init_postgres_client, close_postgres_client
from core.redis.access import init_redis_client, close_redis_client
from core.settings import settings
from internal import init_routers


@asynccontextmanager
async def lifespan(
        _app: FastAPI
) -> AsyncGenerator:
    init_logger()
    await init_minio_client()
    await init_postgres_client()
    await init_redis_client()
    logger.info("All resources have been successfully initialized")
    yield
    await close_minio_client()
    await close_postgres_client()
    await close_redis_client()
    logger.info("All resources have been successfully closed")


def init_app() -> FastAPI:
    _app = FastAPI(
        title="undefined",
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
