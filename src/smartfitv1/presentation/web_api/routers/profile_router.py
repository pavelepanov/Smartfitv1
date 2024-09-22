from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from src.smartfitv1.application.contracts.profiles.requests import \
    CreateProfileRequest
from src.smartfitv1.application.contracts.profiles.responses import \
    ProfileResponse
from src.smartfitv1.application.usecases.create_profile import CreateProfile
from src.smartfitv1.presentation.web_api.schemas.profiles import \
    ProfileCreateSchema

profile_router = APIRouter(tags=["profile"], route_class=DishkaRoute)


@profile_router.post(
    "/profile", response_model=ProfileResponse, description="Create profile"
)
async def create_profile(
    schema: ProfileCreateSchema, interactor: FromDishka[CreateProfile]
) -> ProfileResponse:
    return await interactor(
        CreateProfileRequest(
            name=schema.name,
            age=schema.age,
            user_id=schema.user_id,
        )
    )
