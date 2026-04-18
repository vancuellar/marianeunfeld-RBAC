from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    APP_NAME: str = "Maria Neunfeld RBAC API"
    SECRET_KEY: str = "change-me-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DATABASE_URL: str = "sqlite:///./dev.db"

    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    MAIL_USERNAME: str = ""
    MAIL_PASSWORD: str = ""
    NOTIFY_EMAIL: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
