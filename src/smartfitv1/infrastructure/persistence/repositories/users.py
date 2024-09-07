from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.smartfitv1.domain.users.entities import User
from src.smartfitv1.domain.users.repositories import UserRepository
from src.smartfitv1.domain.users.value_objects import UserId
from src.smartfitv1.infrastructure.persistence.models.user import UserDb
from src.smartfitv1.infrastructure.persistence.repositories.mappers.users import (
    user_db_model_to_user_sdto,
)


class SqlalchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, user_id: UserId) -> User | None:
        query = select(UserDb).where(UserDb.id == user_id.value)
        result = await self.session.execute(query)
        user: UserDb | None = result.scalar()

        return user_db_model_to_user_sdto(user)
