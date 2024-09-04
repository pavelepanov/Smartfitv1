import datetime
from typing import Annotated

from sqlalchemy.orm import mapped_column
from sqlalchemy import text


intpk = Annotated[int, mapped_column(primary_key=True)]