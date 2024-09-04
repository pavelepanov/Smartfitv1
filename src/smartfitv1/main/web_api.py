from dishka.integrations.fastapi import setup_dishka, inject, FromDishka
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from contextlib import asynccontextmanager

from src.smartfitv1.infrastructure.di.main import container_factory
from src.smartfitv1.presentation.web_api.exc_handlers import init_exception_handlers
#from src.smartfitv1.infrastructure.auth.main import auth_backend
from src.smartfitv1.infrastructure.data_access.models.user import UserDb
from src.smartfitv1.infrastructure.auth.manager import get_user_manager, auth_backend
from src.smartfitv1.presentation.web_api.schemas.auth import UserRead, UserCreate
from src.smartfitv1.infrastructure.di.main import container_factory
from src.smartfitv1.presentation.web_api.check import check_router
from src.smartfitv1.infrastructure.auth.manager import fastapi_users

def init_di(app: FastAPI) -> None:
    setup_dishka(container_factory(), app)


def init_routers(app: FastAPI) -> None:

    app.include_router(
        fastapi_users.get_auth_router(FromDishka[auth_backend]),
        prefix="/auth/jwt",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["auth"],
    )

    app.include_router(check_router)

def create_app() -> FastAPI:
    app = FastAPI()

    init_di(app)
    init_routers(app)
    init_exception_handlers(app)

    return app