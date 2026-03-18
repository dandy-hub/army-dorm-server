from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    host: str = "localhost"
    port: int = 5432
    name: str = "mydb"


class Settings(BaseSettings):
    app_name: str = "Army dorms"
    debug: bool = False
    port: int = 8080
    database: DatabaseConfig = DatabaseConfig()
    model_config = SettingsConfigDict(env_file=".env", extra="forbid")


@lru_cache
def get_settings() -> Settings:
    return Settings()
