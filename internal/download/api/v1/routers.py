from fastapi import APIRouter, Depends
from fastapi.responses import Response

from core.minio.client import MinIOClient
from core.minio.access import get_minio_client

router = APIRouter(
    prefix="/api/download",
    tags=["Download"]
)


@router.get(
    "/{path:path}"
)
async def download_file(
        path: str,
        minio_client: 'MinIOClient' = Depends(get_minio_client)
) -> Response:
    file_content = await minio_client.get_object(path)
    headers = {
        "Content-Disposition": f"attachment; filename={path.split('/')[-1]}",
        "Content-Type": "application/octet-stream"
    }
    return Response(
        content=file_content,
        headers=headers
    )
