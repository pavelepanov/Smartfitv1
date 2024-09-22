from pydantic import BaseModel


class ProfileCreateSchema(BaseModel):
    name: str
    age: int
    user_id: int
