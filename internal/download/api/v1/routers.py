from fastapi import APIRouter, Depends
from fastapi.responses import Response

from infra.minio.client import MinIOClient
from infra.minio.access import get_minio_client
from pkg.exceptions import CustomExceptionResponse, handle_exception
from internal.download.usecase.usecase import DownloadUsecase

router = APIRouter(
    prefix="/api/download",
    tags=["Download"]
)


@router.get(
    "/{path:path}",
    status_code=200,
    response_class=Response,
    responses={
        404: {"model": CustomExceptionResponse}
    }
)
async def download_file(
        path: str,
        minio_client: 'MinIOClient' = Depends(get_minio_client)
) -> Response:
    download_usecase = DownloadUsecase(minio_client)
    try:
        file_content = await download_usecase.get_file_content(path)
        headers = {
            "Content-Disposition": f"attachment; filename={path.split('/')[-1]}",
            "Content-Type": "application/octet-stream"
        }
        return Response(
            content=file_content,
            headers=headers
        )
    except Exception as e:
        handle_exception(e)
