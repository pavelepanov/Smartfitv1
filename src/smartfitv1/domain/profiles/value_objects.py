from dataclasses import dataclass

from src.smartfitv1.domain.common.exceptions import ValueObjectValidationError
from src.smartfitv1.domain.common.value_objects import BaseValueObject


@dataclass(frozen=True)
class ProfileId(BaseValueObject):
    value: int

    def _validate(self) -> None:
        if not isinstance(self.value, int):
            raise ValueObjectValidationError("Id must be an int")


@dataclass(frozen=True)
class ProfileName(BaseValueObject):
    value: str

    def _validate(self) -> None:
        if not isinstance(self.value, str):
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
class ProfileAge(BaseValueObject):
    value: int

    def _validate(self) -> None:
        if not isinstance(self.value, int):
            raise ValueObjectValidationError("Age must be an int")
        if self.value <= 0:
            raise ValueObjectValidationError("Age must be over 0")
