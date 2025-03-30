from contextlib import asynccontextmanager
from typing import Dict

from aiobotocore.session import get_session, AioSession
from types_aiobotocore_s3.client import S3Client
from botocore.exceptions import ClientError

from core.logger import logger
from core.settings import settings


class MinIOClient:
    config: Dict | None = None
    bucket_name: str | None = None
    session: AioSession | None = None

    @classmethod
    async def init_client(
            cls
    ) -> None:
        if cls.session is not None:
            logger.error("MinIO is already initialized")
            return

        cls.config = {
            "endpoint_url": settings.minio_url,
            "aws_access_key_id": settings.minio_access_key,
            "aws_secret_access_key": settings.minio_secret_key,
            "aws_session_token": None if settings.minio_session_token == "None" else settings.minio_session_token,
            "region_name": settings.minio_region_name,
            "verify": None if settings.minio_verify == "None" else settings.minio_verify,
            "use_ssl": settings.minio_secure
        }
        cls.bucket_name = settings.minio_bucket
        cls.session = get_session()

        logger.info("MinIO initialized")

    @classmethod
    async def close_client(
            cls
    ) -> None:
        if cls.config is None or cls.bucket_name is None or cls.session is None:
            logger.error("MinIO is not initialized")
            return

        cls.config = None
        cls.bucket_name = None
        cls.session = None

        logger.info("MinIO closed")

    @classmethod
    @asynccontextmanager
    async def get_client(
            cls
    ) -> S3Client:
        async with cls.session.create_client(
                "s3",
                **cls.config
        ) as client:
            yield client

    @classmethod
    async def upload_object(
            cls,
            object_name: str,
            content: bytes
    ) -> None:
        async with cls.get_client() as client:
            await client.put_object(
                Bucket=cls.bucket_name,
                Key=object_name,
                Body=content
            )

    @classmethod
    async def get_object(
            cls,
            object_name: str
    ) -> bytes | None:
        async with cls.get_client() as client:
            try:
                response = await client.get_object(
                    Bucket=cls.bucket_name,
                    Key=object_name
                )
                return await response["Body"].read()
            except ClientError as e:
                logger.error(f"Error getting object: {e.response["Error"]["Message"]}")
                return None

    @classmethod
    async def delete_object(
            cls,
            object_name: str
    ) -> None:
        async with cls.get_client() as client:
            await client.delete_object(
                Bucket=cls.bucket_name,
                Key=object_name
            )

    @classmethod
    def get_instance(
            cls
    ) -> 'MinIOClient':
        return cls()
