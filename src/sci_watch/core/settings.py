import os
from typing import Literal, Optional

from pydantic import Field, ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings class, loaded from .env file
    """
    model_config = ConfigDict(extra='ignore', frozen=True)
    
    log_level: Literal[
        "NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "FATAL", "CRITICAL"
    ] = Field(default="DEBUG")
    gmail_sender: str
    gmail_token: str 
    grammar_path: str
    http_proxy: Optional[str] = Field(default=None)
    https_proxy: Optional[str] = Field(default=None)
    log_file_path: Optional[str] = Field(default=None)


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")

if settings.log_level in ["NOTSET", "DEBUG"]:
    print("Settings config: ", settings.dict())
