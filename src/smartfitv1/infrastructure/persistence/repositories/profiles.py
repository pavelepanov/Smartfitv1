from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.smartfitv1.domain.profiles.entities import Profile, profile_factory
from src.smartfitv1.domain.profiles.value_objects import (ProfileAge,
                                                          ProfileName)
from src.smartfitv1.domain.users.repositories import UserRepository
from src.smartfitv1.domain.users.value_objects import UserId
from src.smartfitv1.infrastructure.persistence.models.profile import ProfileDb


class SqlalchemyProfileRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(
        self, name: ProfileName, age: ProfileAge, user_id: UserId
    ) -> Profile:
        stmt = (
            insert(ProfileDb)
            .values(
                name=name.value,
                age=age.value,
                user_id=user_id.value,
            )
            .returning(
                ProfileDb.id,
                ProfileDb.name,
                ProfileDb.age,
                ProfileDb.user_id,
            )
        )

        result = await self.session.execute(stmt)
        await self.session.commit()

        profile = result.mappings().first()

        return profile_factory(
            id=profile.id,
            name=profile.name,
            age=profile.age,
            user_id=profile.user_id,
        )
