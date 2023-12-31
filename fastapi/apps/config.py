from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


@lru_cache
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding='utf-8')
    APP_NAME: str = "Todo App"
    DEBUG_MODE: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DB_URL: str
    DB_NAME: str
    ALLOW_ORIGINS:str


settings = Settings()
