from typing import cast

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.types import ExceptionHandler


class WebApiError(Exception):
    message: str

    def __init__(self, message: str | None = None) -> None:
        super().__init__()

        if message is None:
            assert hasattr(self, "message")

        else:
            self.message = message


async def domain_validation_handler(exc: WebApiError) -> JSONResponse:
    return JSONResponse(status_code=422, content={"message": exc.message})


def init_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        WebApiError, cast(ExceptionHandler, domain_validation_handler)
    )
