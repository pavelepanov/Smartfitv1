from src.smartfitv1.application.contracts.users.requests import GetUserByIdRequest
from src.smartfitv1.application.contracts.users.responses import UserResponse
from src.smartfitv1.application.protocols.interactor import Interactor
from src.smartfitv1.domain.users.repositories import UserRepository
from src.smartfitv1.domain.users.value_objects import UserId


class GetUserById(Interactor[GetUserByIdRequest, UserResponse]):
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def __call__(self, request: GetUserByIdRequest) -> UserResponse:
        user = await self.user_repository.get_by_id(user_id=UserId(request.id))

        return UserResponse(
            id=user.id.value,
            email=user.email.value,
            hashed_password=user.hashed_password.value,
        )
