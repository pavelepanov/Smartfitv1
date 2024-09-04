from dataclasses import dataclass, field

from fastapi import APIRouter, Depends
from src.smartfitv1.infrastructure.data_access.models.user import UserDb
from src.smartfitv1.infrastructure.auth.manager import current_user

check_router = APIRouter(prefix="/check", tags=["check"])


@dataclass(frozen=True)
class Check:
    status: str = field(default="ok")


@check_router.get("/", response_model=Check)
async def health_check(user: UserDb = Depends(current_user)) -> Check:
    return Check(status="ok")