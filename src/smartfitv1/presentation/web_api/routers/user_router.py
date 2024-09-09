from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from src.smartfitv1.application.contracts.users.requests import \
    GetUserByIdRequest
from src.smartfitv1.application.contracts.users.responses import UserResponse
from src.smartfitv1.application.usecases.get_user_by_id import GetUserById

user_router = APIRouter(tags=["user"], route_class=DishkaRoute)


@user_router.get(
    "/user/{user_id}", response_model=UserResponse, description="Get user by id"
)
async def create_user(
    user_id: int, interactor: FromDishka[GetUserById]
) -> UserResponse:
    return await interactor(
        GetUserByIdRequest(
            id=user_id,
        )
    )
