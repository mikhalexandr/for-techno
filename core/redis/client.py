import redis.asyncio as redis

from core.logger import logger
from core.settings import settings


class RedisClient:
    _client: redis.Redis | None = None

    @classmethod
    async def init_client(
            cls
    ) -> None:
        if cls._client is not None:
            logger.error("Redis is already initialized")
            return None

        cls._client = redis.from_url(settings.get_redis_url())
        logger.info("Redis initialized")

    @classmethod
    async def close_client(
            cls
    ) -> None:
        if cls._client is not None:
            await cls._client.close()
            cls._client = None
            logger.info("Redis closed")

    @classmethod
    def get_client(
            cls
    ) -> redis.Redis:
        return cls._client
