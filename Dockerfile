FROM python:3.12.3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /smartfitv1

WORKDIR /smartfitv1

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

COPY conf /smartfitv1/conf
COPY src /smartfitv1/src
COPY alembic.ini /smartfitv1