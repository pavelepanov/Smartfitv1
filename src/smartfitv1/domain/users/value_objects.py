import re
from dataclasses import dataclass

from src.smartfitv1.domain.common.exceptions import ValueObjectValidationError
from src.smartfitv1.domain.common.value_objects import ValueObject


@dataclass(frozen=True)
class UserId(ValueObject):
    value: int

    def _validate(self) -> None:
        if not isinstance(self.to_raw(), int):
            raise ValueObjectValidationError("Id must be an int")


@dataclass(frozen=True)
class UserEmail(ValueObject):
    value: str

    def _validate(self) -> None:
        pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"

        if not isinstance(self.to_raw(), str):
            raise ValueObjectValidationError("Email must be an str")
        if not re.match(pattern, self.value):
            raise ValueObjectValidationError(
                "Invalid email format. Email must be in the format 'example@example.com'."
            )
        if len(self.value) > 320:
            raise ValueObjectValidationError("Email must be less than 320 symbols")


@dataclass(frozen=True)
class UserName(ValueObject):
    value: str

    def _validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise ValueObjectValidationError("Name must be an str")
        if len(self.value) < 1:
            raise ValueObjectValidationError("Name must be at least 1 character long.")
        if len(self.value) > 100:
            raise ValueObjectValidationError(
                "Name must be at most 100 characters long."
            )
        if not self.value.isalpha():
            raise ValueObjectValidationError("Name must only contain letters.")


@dataclass(frozen=True)
class UserAge(ValueObject):
    value: int

    def _validate(self) -> None:
        if not isinstance(self.to_raw(), int):
            raise ValueObjectValidationError("Age must be an int")
        if self.value <= 0:
            raise ValueObjectValidationError("Age must be over 0")


@dataclass(frozen=True)
class UserHashedPassword(ValueObject):
    value: str

    def _validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise ValueObjectValidationError("Hashed password must be a str")
        if len(self.value) > 1024:
            raise ValueObjectValidationError(
                "Hashed password must be less then 1024 symbols"
            )
