from dishka import AsyncContainer, make_async_container

from src.smartfitv1.infrastructure.di.providers.adapters import (
    FastapiUsersProvider,
    SqlalchemyProvider,
)


def container_factory() -> AsyncContainer:
    return make_async_container(SqlalchemyProvider(), FastapiUsersProvider())
