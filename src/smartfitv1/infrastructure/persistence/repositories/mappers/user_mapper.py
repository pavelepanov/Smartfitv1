from src.smartfitv1.domain.users.entities import User
from src.smartfitv1.domain.users.value_objects import (
    UserEmail,
    UserHashedPassword,
    UserId,
)
from src.smartfitv1.infrastructure.persistence.models.user import UserDb


def user_from_db_to_entity(user: UserDb) -> User:
    return User(
        id=UserId(user.id),
        email=UserEmail(user.email),
        hashed_password=UserHashedPassword(user.hashed_password),
    )
