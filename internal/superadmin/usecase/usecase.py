from sqlalchemy.ext.asyncio import AsyncSession

from internal.superadmin.repository.repository import SuperadminRepository
from internal.superadmin.schemes.superadmin import SuperadminRs, SuperadminCreateRq, SuperadminUpdateRq


class SuperadminUsecase:
    def __init__(
            self,
            db_session: AsyncSession
    ):
        self.repo = SuperadminRepository(db_session)

    async def create_user(
            self,
            user: SuperadminCreateRq
    ) -> SuperadminRs:
        return await self.repo.create_user(user)

    async def update_user(
            self,
            user: SuperadminUpdateRq
    ) -> SuperadminRs:
        return await self.repo.update_user(user)

    async def delete_user(
            self,
            user_id: str
    ) -> SuperadminRs:
        return await self.repo.delete_user(user_id)
