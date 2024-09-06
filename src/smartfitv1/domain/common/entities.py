from dataclasses import dataclass
from typing import Generic, TypeVar

from src.smartfitv1.domain.common.value_objects import ValueObject

DomainEntityId = TypeVar("DomainEntityId", bound=ValueObject)


@dataclass(frozen=True)
class DomainEntity(Generic[DomainEntityId]):
    id: DomainEntityId

    def __eq__(self, other):
        if isinstance(other, DomainEntity):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
