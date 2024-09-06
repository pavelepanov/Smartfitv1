class DomainError(Exception):
    message: str

    def __init__(self, message: str | None = None) -> None:
        super().__init__()

        if message is None:
            assert hasattr(
                self, "message"
            ), "Message must be specified in the constructor or class var"

        else:
            self.message = message


class ValueObjectValidationError(DomainError):
    pass


class EntityValidationError(DomainError):
    pass
