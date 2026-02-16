from pydantic_settings import BaseSettings

class settings(BaseSettings):
    DATABASE_URL: str

settings = settings()