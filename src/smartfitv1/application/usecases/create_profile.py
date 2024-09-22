from src.smartfitv1.application.contracts.profiles.requests import \
    CreateProfileRequest
from src.smartfitv1.application.contracts.profiles.responses import \
    ProfileResponse
from src.smartfitv1.application.protocols.interactor import Interactor
from src.smartfitv1.domain.profiles.repositories import ProfileRepository
from src.smartfitv1.domain.profiles.value_objects import (ProfileAge,
                                                          ProfileName)
from src.smartfitv1.domain.users.value_objects import UserId


class CreateProfile(Interactor[CreateProfileRequest, ProfileResponse]):
    def __init__(self, profile_repository: ProfileRepository) -> None:
        self.profile_repository = profile_repository

    async def __call__(self, request: CreateProfileRequest) -> ProfileResponse:
        profile = await self.profile_repository.create(
            name=ProfileName(request.name),
            age=ProfileAge(request.age),
            user_id=UserId(request.user_id),
        )

        return ProfileResponse(
            id=profile.id.value,
            name=profile.name.value,
            age=profile.age.value,
            user_id=profile.user_id.value,
        )
