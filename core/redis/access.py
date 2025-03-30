import redis.asyncio as redis

from core.redis.client import RedisClient


async def init_redis_client() -> None:
    await RedisClient.init_client()


async def close_redis_client() -> None:
    await RedisClient.close_client()


async def get_redis_client() -> redis.Redis:
    return RedisClient.get_client()
