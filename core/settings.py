from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER:str
    POSTGRES_PASSWORD:str
    POSTGRES_DB:str
    DB_URL: str
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    MY_IP: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()