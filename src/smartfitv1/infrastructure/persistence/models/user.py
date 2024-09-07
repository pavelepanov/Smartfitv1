from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.smartfitv1.infrastructure.persistence.models.base import BaseDb
from src.smartfitv1.infrastructure.persistence.models.types.created_at import created_at
from src.smartfitv1.infrastructure.persistence.models.types.int_pk import intpk
from src.smartfitv1.infrastructure.persistence.models.types.updated_at import updated_at


class UserDb(SQLAlchemyBaseUserTable[int], BaseDb):
    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String, default="")
    age: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
