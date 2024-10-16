from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import ClassVar, Optional
import os

load_dotenv()

class Settings(BaseSettings):
    DB_HOST: ClassVar[Optional[str]] = os.getenv("DB_HOST")
    DB_USER: ClassVar[Optional[str]] = os.getenv("DB_USER")
    DB_PASSWORD: ClassVar[Optional[str]] = os.getenv("DB_PASSWORD")
    DB_PORT: ClassVar[Optional[str]] = os.getenv("DB_PORT")
    DB_NAME: ClassVar[Optional[str]] = os.getenv("DB_NAME")

    DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

    print(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

settings = Settings()
