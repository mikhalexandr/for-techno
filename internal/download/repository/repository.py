from infra.minio.client import MinIOClient
from infra.logger import logger
from pkg.exceptions import CustomException


class DownloadRepository:
    def __init__(
            self,
            minio_client: 'MinIOClient'
    ):
        self.minio_client = minio_client

    async def get_file_content(
            self,
            path: str
    ) -> bytes:
        try:
            file_content = await self.minio_client.get_object(path)
            logger.info(f"Getting file content: {file_content}")
            return file_content
        except Exception as e:
            logger.error(f"Error getting file content: {e}")
            raise CustomException(404, "error", f"File not found")
