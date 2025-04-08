from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from infra.postgres.access import get_async_session
from internal.user.schemes.users import UserRegisterRq, UserRegisterRs
from pkg.exceptions import handle_exception
from internal.user.usecase.usecase import UserUsecase

router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)


@router.post(
    "/register",
    status_code=200,
    response_model=UserRegisterRs,
    include_in_schema=False,
)
async def register_user(
        user: UserRegisterRq,
        db_session: AsyncSession = Depends(get_async_session)
) -> UserRegisterRs:
    user_usecase = UserUsecase(db_session)
    try:
        reg_user = await user_usecase.register_user(user)
        return reg_user
    except Exception as e:
        handle_exception(e)
