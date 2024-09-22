from dataclasses import dataclass

from src.smartfitv1.domain.common.entities import DomainEntity
from src.smartfitv1.domain.users.value_objects import (UserEmail,
                                                       UserHashedPassword,
                                                       UserId)


@dataclass
class User(DomainEntity[UserId]):
    id: UserId
    email: UserEmail
    hashed_password: UserHashedPassword


def user_factory(
    id: int,
    email: str,
    hashed_password: str,
) -> User:
    return User(
        id=UserId(id),
        email=UserEmail(email),
        hashed_password=UserHashedPassword(hashed_password),
    )
