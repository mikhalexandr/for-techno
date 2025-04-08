from sqlalchemy.ext.asyncio import AsyncSession

from internal.user.schemes.users import UserRegisterRq, UserRegisterRs
from internal.user.repository.repository import UserRepository


class UserUsecase:
    def __init__(
            self,
            db_session: AsyncSession
    ):
        self.repo = UserRepository(db_session)

    async def register_user(
            self,
            user: UserRegisterRq
    ) -> UserRegisterRs:
        return await self.repo.register_user(user)
