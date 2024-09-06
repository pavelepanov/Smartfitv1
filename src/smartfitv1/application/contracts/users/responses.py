from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class UserResponse:
    id: int
    name: str
    age: int
    email: str
    hashed_password: str
    created_at: datetime
    updated_at: datetime
