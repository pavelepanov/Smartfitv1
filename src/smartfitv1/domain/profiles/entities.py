from dataclasses import dataclass

from src.smartfitv1.domain.common.entities import DomainEntity
from src.smartfitv1.domain.profiles.value_objects import (ProfileAge,
                                                          ProfileId,
                                                          ProfileName)
from src.smartfitv1.domain.users.value_objects import UserId


@dataclass
class Profile(DomainEntity[ProfileId]):
    id: ProfileId
    name: ProfileName
    age: ProfileAge
    user_id: UserId


def profile_factory(
    id: int,
    name: str,
    age: int,
    user_id: int,
) -> Profile:
    return Profile(
        id=ProfileId(id),
        name=ProfileName(name),
        age=ProfileAge(age),
        user_id=UserId(user_id),
    )
