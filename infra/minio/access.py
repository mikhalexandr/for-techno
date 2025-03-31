from infra.minio.client import MinIOClient


async def init_minio_client() -> None:
    await MinIOClient.init_client()


async def close_minio_client() -> None:
    await MinIOClient.close_client()


async def get_minio_client() -> 'MinIOClient':
    return MinIOClient.get_instance()
