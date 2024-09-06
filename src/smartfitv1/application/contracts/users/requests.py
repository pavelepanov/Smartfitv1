from dataclasses import dataclass


@dataclass(frozen=True)
class GetUserByIdRequest:
    id: int
