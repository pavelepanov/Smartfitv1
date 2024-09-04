from typing import AsyncGenerator

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from src.smartfitv1.infrastructure.data_access.models.base import BaseDb
from src.smartfitv1.infrastructure.data_access.models.types.int_pk import intpk


class UserDb(SQLAlchemyBaseUserTable[int], BaseDb):
    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )


#async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#    yield SQLAlchemyUserDatabase(session, UserDb)
