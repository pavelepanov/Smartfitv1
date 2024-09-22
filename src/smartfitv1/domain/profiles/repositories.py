from typing import Protocol

from src.smartfitv1.domain.profiles.entities import Profile
from src.smartfitv1.domain.profiles.value_objects import (ProfileAge,
                                                          ProfileName)
from src.smartfitv1.domain.users.value_objects import UserId


class ProfileRepository(Protocol):
    async def create(
        self, name: ProfileName, age: ProfileAge, user_id: UserId
    ) -> Profile:
        raise NotImplementedError
