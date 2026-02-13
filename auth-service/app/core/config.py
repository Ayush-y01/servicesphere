from pydantic_settings import BaseSettings

class settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:ayush890@localhost:5432/auth_db"

settings = settings()