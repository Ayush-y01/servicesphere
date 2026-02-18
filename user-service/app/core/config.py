from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    AUTH_SERVICE_URL: str = "http://auth-service:8001"
    JWT_ALGORITHM: str = "HS256"
    JWT_SECRET_KEY: str = "supersecret"  # later env me jayega

    class config:
        env_file = ".env"

settings = Settings()