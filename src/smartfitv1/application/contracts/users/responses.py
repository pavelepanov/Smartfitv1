from dataclasses import dataclass


@dataclass(frozen=True)
class UserResponse:
    id: int
    email: str
    hashed_password: str
