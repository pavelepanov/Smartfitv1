from dishka import Provider, Scope, provide

from src.smartfitv1.application.usecases.get_user_by_id import GetUserById


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    get_user_by_id = provide(GetUserById)
