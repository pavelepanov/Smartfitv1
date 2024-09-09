from dishka.integrations.fastapi import FromDishka, setup_dishka
from fastapi import FastAPI

# from src.smartfitv1.infrastructure.auth.main import auth_backend
from src.smartfitv1.infrastructure.auth.manager import (auth_backend,
                                                        fastapi_users)
from src.smartfitv1.infrastructure.di.main import container_factory
from src.smartfitv1.presentation.web_api.exc_handlers import \
    init_exception_handlers
from src.smartfitv1.presentation.web_api.routers.user_router import user_router
from src.smartfitv1.presentation.web_api.schemas.auth import (UserCreate,
                                                              UserRead)


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

    app.include_router(user_router)


def create_app() -> FastAPI:
    app = FastAPI()

    init_di(app)
    init_routers(app)
    init_exception_handlers(app)

    return app
