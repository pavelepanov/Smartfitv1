from dataclasses import dataclass


@dataclass(frozen=True)
class ProfileResponse:
    id: int
    name: str
    age: int
    user_id: int
