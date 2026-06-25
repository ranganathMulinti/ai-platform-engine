"""
Application configuration.

All application settings are loaded from environment variables using
Pydantic Settings.
"""

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

from .environment import Environment


class Settings(BaseSettings):
    """
    Application settings.

    Values can be overridden using environment variables with the
    AI_PLATFORM_ prefix.

    Example:

        AI_PLATFORM_DATABASE_URL=postgresql://...
        AI_PLATFORM_SECRET_KEY=...
    """

    # ==========================================================
    # Application
    # ==========================================================

    app_name: str = "AI Platform Engine"

    app_version: str = "0.1.0"

    environment: Environment = Environment.development

    debug: bool = True

    host: str = "0.0.0.0"

    port: int = 8000

    # ==========================================================
    # Database
    # ==========================================================

    database_url: str = "sqlite:///./test.db"

    # ==========================================================
    # Redis
    # ==========================================================

    redis_url: str = "redis://localhost:6379"

    gemini_api_key: str = ""

    default_llm_model: str = "gemini-2.5-flash"

    # ==========================================================
    # Authentication
    # ==========================================================

    secret_key: str = "change-me-in-production-use-a-long-random-secret"

    algorithm: str = "HS256"

    access_token_expire_minutes: int = 30

    # ==========================================================
    # Logging
    # ==========================================================

    log_level: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ] = "INFO"

    # ==========================================================
    # Pydantic Settings
    # ==========================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="AI_PLATFORM_",
        extra="ignore",
    )
