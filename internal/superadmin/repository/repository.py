from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete
from sqlalchemy.dialects.postgresql import insert

from internal.user.models.users import UserModel
from internal.superadmin.schemes.superadmin import SuperadminRs, SuperadminCreateRq, SuperadminUpdateRq


class SuperadminRepository:
    def __init__(
            self,
            db_session: AsyncSession
    ):
        self.db_session = db_session

    async def create_user(
            self,
            user: SuperadminCreateRq
    ) -> SuperadminRs:
        stmt = insert(UserModel).values(
            id=user.id,
            name=user.userName,
            email=user.email
        )
        await self.db_session.execute(stmt)
        await self.db_session.commit()
        return SuperadminRs(
            status="OK"
        )

    async def update_user(
            self,
            user: SuperadminUpdateRq
    ) -> SuperadminRs:
        stmt = update(UserModel).where(UserModel.id == user.id).values(
            email=user.email
        )
        await self.db_session.execute(stmt)
        await self.db_session.commit()
        return SuperadminRs(
            status="OK"
        )

    async def delete_user(
            self,
            user_id: str
    ) -> SuperadminRs:
        stmt = delete(UserModel).where(UserModel.id == user_id)
        await self.db_session.execute(stmt)
        await self.db_session.commit()
        return SuperadminRs(
            status="OK"
        )
