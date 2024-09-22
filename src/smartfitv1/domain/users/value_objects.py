import re
from dataclasses import dataclass

from src.smartfitv1.domain.common.exceptions import ValueObjectValidationError
from src.smartfitv1.domain.common.value_objects import BaseValueObject


@dataclass(frozen=True)
class UserId(BaseValueObject):
    value: int

    def _validate(self) -> None:
        if not isinstance(self.value, int):
            raise ValueObjectValidationError("Id must be an int")


@dataclass(frozen=True)
class UserEmail(BaseValueObject):
    value: str

    def _validate(self) -> None:
        pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"

        if not isinstance(self.value, str):
            raise ValueObjectValidationError("Email must be an str")
        if not re.match(pattern, self.value):
            raise ValueObjectValidationError(
                "Invalid email format. Email must be in the format 'example@example.com'."
            )
        if len(self.value) > 320:
            raise ValueObjectValidationError("Email must be less than 320 symbols")


@dataclass(frozen=True)
class UserHashedPassword(BaseValueObject):
    value: str

    def _validate(self) -> None:
        if not isinstance(self.value, str):
            raise ValueObjectValidationError("Hashed password must be a str")
        if len(self.value) > 1024:
            raise ValueObjectValidationError(
                "Hashed password must be less then 1024 symbols"
            )
