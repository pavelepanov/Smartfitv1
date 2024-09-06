from dataclasses import dataclass
from datetime import datetime

from src.smartfitv1.domain.common.entities import DomainEntity
from src.smartfitv1.domain.users.value_objects import (UserAge, UserEmail,
                                                       UserHashedPassword,
                                                       UserId, UserName)


@dataclass(frozen=True)
class User(DomainEntity[UserId]):
    name: UserName
    age: UserAge
    email: UserEmail
    hashed_password: UserHashedPassword
    created_at: datetime
    updated_at: datetime


def user_factory(
    id: int,
    name: str,
    age: int,
    email: str,
    hashed_password: str,
    created_at: datetime,
    updated_at: datetime,
) -> User:
    return User(
        id=UserId(id),
        name=UserName(name),
        age=UserAge(age),
        email=UserEmail(email),
        hashed_password=UserHashedPassword(hashed_password),
        created_at=created_at,
        updated_at=updated_at,
    )
