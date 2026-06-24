from typing import Literal

from pydantic_settings import BaseSettings

from .environment import Environment


class Settings(BaseSettings):
    app_name: str = "AI Platform Engine"
    app_version: str = "0.1.0"
    environment: Environment = Environment.development
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    database_url: str = "sqlite:///./test.db"
    redis_url: str = "redis://localhost:6379"
    secret_key: str = "secret_key"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    class SettingsConfigDict:
        env_file = ".env"
        env_prefix = "AI_PLATFORM_"
