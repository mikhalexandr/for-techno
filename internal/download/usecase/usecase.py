from infra.minio.client import MinIOClient
from internal.download.repository.repository import DownloadRepository


class DownloadUsecase:
    def __init__(
            self,
            minio_client: 'MinIOClient'
    ):
        self.repo = DownloadRepository(
            minio_client
        )

    async def get_file_content(
            self,
            path: str
    ) -> bytes:
        return await self.repo.get_file_content(path)
