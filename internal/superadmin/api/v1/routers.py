from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from infra.postgres.access import get_async_session
from internal.superadmin.schemes.superadmin import SuperadminRs, SuperadminCreateRq, SuperadminUpdateRq
from pkg.exceptions import handle_exception
from internal.superadmin.usecase.usecase import SuperadminUsecase

router = APIRouter(
    prefix="/api/superadmin",
    tags=["Superadmin"]
)


@router.post(
    "/create",
    status_code=200,
    response_model=SuperadminRs,
    include_in_schema=False,
)
async def create_user(
        user: SuperadminCreateRq,
        db_session: AsyncSession = Depends(get_async_session)
) -> SuperadminRs:
    superadmin_usecase = SuperadminUsecase(db_session)
    try:
        cr_user = await superadmin_usecase.create_user(user)
        return cr_user
    except Exception as e:
        handle_exception(e)


@router.patch(
    "/update",
    status_code=200,
    response_model=SuperadminRs,
    include_in_schema=False,
)
async def update_user(
        user: SuperadminUpdateRq,
        db_session: AsyncSession = Depends(get_async_session)
) -> SuperadminRs:
    superadmin_usecase = SuperadminUsecase(db_session)
    try:
        upd_user = await superadmin_usecase.update_user(user)
        return upd_user
    except Exception as e:
        handle_exception(e)


@router.delete(
    "/delete/{user_id}",
    status_code=200,
    response_model=SuperadminRs,
    include_in_schema=False,
)
async def delete_user(
        user_id: str,
        db_session: AsyncSession = Depends(get_async_session)
) -> SuperadminRs:
    superadmin_usecase = SuperadminUsecase(db_session)
    try:
        del_user = await superadmin_usecase.delete_user(user_id)
        return del_user
    except Exception as e:
        handle_exception(e)
