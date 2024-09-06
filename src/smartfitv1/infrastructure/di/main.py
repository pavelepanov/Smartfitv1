from dishka import AsyncContainer, make_async_container

from src.smartfitv1.infrastructure.di.providers.adapters import (
    FastapiUsersProvider, SqlalchemyProvider)
from src.smartfitv1.infrastructure.di.providers.usecases import \
    UseCasesProvider


def container_factory() -> AsyncContainer:
    return make_async_container(
        SqlalchemyProvider(), UseCasesProvider(), FastapiUsersProvider()
    )
