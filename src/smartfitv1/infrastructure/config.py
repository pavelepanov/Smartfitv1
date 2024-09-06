from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class DatabaseConfig:
    db_uri: str

    @staticmethod
    def from_env() -> "DatabaseConfig":
        uri = getenv("DATABASE_URI")

        return DatabaseConfig(str(uri))


@dataclass(frozen=True)
class SecretJwtConfig:
    secret_jwt: str

    @staticmethod
    def from_env() -> "SecretJwtConfig":
        secret = getenv("SECRET_JWT")

        return SecretJwtConfig(str(secret))


@dataclass(frozen=True)
class SecretManagerConfig:
    secret_manager: str

    @staticmethod
    def from_env() -> "SecretManagerConfig":
        secret = getenv("SECRET_MANAGER")

        return SecretManagerConfig(str(secret))
