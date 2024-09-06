from typing import Protocol

from src.smartfitv1.domain.users.entities import User, UserId


class UserRepository(Protocol):
    async def get_by_id(self, user_id: UserId) -> User:
        raise NotImplementedError
