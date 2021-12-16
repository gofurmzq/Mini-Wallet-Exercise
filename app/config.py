from typing import List
import logging
import os
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    # app config
    DEBUG: bool = False
    PORT: int
    SECRET_KEY: str
    ENABLE_APIDOCS: bool

    LOG_TO_FILE: bool = False
    LOG_LEVEL_INFO: int = logging.INFO
    LOG_LEVEL_WARNING: int = logging.WARNING
    LOG_FILE: list = ['logs/mini_wallet_api_info.log', 'logs/mini_wallet_api_warning.log', 'logs/mini_wallet_api_error.log']
    LOG_LEVEL: list = [logging.INFO, logging.WARNING, logging.ERROR]

    CORS_ALLOW_ORIGINS: str = '*'
    CORS_ALLOW_METHODS: str = '*'
    CORS_ALLOW_HEADERS: str = '*'

    class Config:
        env_file = os.environ.get('ENV_FILE', '.env')
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
