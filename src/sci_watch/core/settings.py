import os
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings class, loaded from .env file
    """

    log_level: Literal[
        "NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "FATAL", "CRITICAL"
    ] = os.getenv("log_level", "DEBUG")
    gmail_sender: str = os.getenv("gmail_sender")
    gmail_token: str = os.getenv("gmail_token")
    grammar_path: str = os.getenv("grammar_path")
    http_proxy: str = os.getenv("http_proxy", None)
    https_proxy: str = os.getenv("https_proxy", None)
    log_file_path: str = os.getenv("log_file_path", None)

    class Config:
        allow_mutation = False


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")

if settings.log_level in ["NOTSET", "DEBUG"]:
    print("Settings config: ", settings.dict())
