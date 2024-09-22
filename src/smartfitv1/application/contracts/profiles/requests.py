from dataclasses import dataclass


@dataclass(frozen=True)
class CreateProfileRequest:
    name: str
    age: int
    user_id: int
