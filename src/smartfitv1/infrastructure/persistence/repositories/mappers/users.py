from src.smartfitv1.domain.users.entities import User
from src.smartfitv1.infrastructure.persistence.models.user import UserDb


def user_db_model_to_user_sdto(user: UserDb) -> User:
    return User(
        id=user.id,
        name=user.name,
        age=user.age,
        email=user.email,
        hashed_password=user.hashed_password,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )
