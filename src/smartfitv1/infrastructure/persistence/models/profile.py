from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.smartfitv1.infrastructure.persistence.models.base import BaseDb
from src.smartfitv1.infrastructure.persistence.models.types.int_pk import intpk

if TYPE_CHECKING:
    from src.smartfitv1.infrastructure.persistence.models.user import UserDb


class ProfileDb(BaseDb):
    __tablename__ = "profile"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["UserDb"] = relationship(back_populates="profile")
