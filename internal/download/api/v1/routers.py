from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response

from infra.minio.client import MinIOClient
from infra.minio.access import get_minio_client

router = APIRouter(
    prefix="/api/download",
    tags=["Download"]
)


@router.get(
    "/{path:path}",
    status_code=200,
    response_class=Response,
    responses={
        200: {"description": "File downloaded successfully"},
        404: {"description": "File not found"}
    }
)
async def download_file(
        path: str,
        minio_client: 'MinIOClient' = Depends(get_minio_client)
) -> Response:
    try:
        file_content = await minio_client.get_object(path)
        headers = {
            "Content-Disposition": f"attachment; filename={path.split('/')[-1]}",
            "Content-Type": "application/octet-stream"
        }
        return Response(
            content=file_content,
            headers=headers
        )
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=f"File not found: {e}"
        )
