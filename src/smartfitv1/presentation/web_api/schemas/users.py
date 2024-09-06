from pydantic import BaseModel


class UserGetByIdSchema(BaseModel):
    id: int
