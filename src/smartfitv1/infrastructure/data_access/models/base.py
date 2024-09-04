from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs


class BaseDb(AsyncAttrs, DeclarativeBase):
    """Base class for all database models."""