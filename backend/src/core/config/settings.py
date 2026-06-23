# settings.py

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """
    Main configuration settings for the AI Platform Engine.

    Attributes:
        database_url (str): The URL of the database.
        secret_key (str): Secret key for security purposes.
        debug_mode (bool): Whether to run in debug mode.
    """

    database_url: str = Field(..., env="DATABASE_URL")
    secret_key: str = Field(..., env="SECRET_KEY")
    debug_mode: bool = Field(False, env="DEBUG_MODE")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
