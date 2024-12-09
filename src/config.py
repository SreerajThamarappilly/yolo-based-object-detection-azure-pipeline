"""
config.py

This file loads configuration from environment variables using pydantic.
It defines a Config class that centralizes the application's configuration.
"""

from pydantic_settings import BaseSettings
from pydantic import Field

class Config(BaseSettings):
    MODEL_PATH: str = Field(...)
    APP_HOST: str = Field("127.0.0.1")
    APP_PORT: int = Field(8000)
    LOG_LEVEL: str = Field("INFO")
    AZURE_CONTAINER_REGISTRY: str = Field(...)
    AZURE_WEBAPP_NAME: str = Field(...)
    PORT: int

    class Config:
        env_file = ".env"
        extra = "allow"

configuration = Config()
