from sqlalchemy.ext.asyncio import AsyncSession

from infra.postgres.client import PostgresClient


async def init_postgres_client() -> None:
    await PostgresClient.init_client()


async def close_postgres_client() -> None:
    await PostgresClient.close_client()


async def get_async_session() -> AsyncSession:
    async_session_maker = PostgresClient.get_async_session()
    async with async_session_maker() as session:
        yield session
