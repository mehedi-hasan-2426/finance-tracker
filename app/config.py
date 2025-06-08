from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "sqlite:///./finance_tracker.db"
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Application
    APP_NAME: str = "Finance Tracker"
    DEBUG: bool = False
    VERSION: str = "0.1.0"
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    
    # Database Pool (PostgreSQL)
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
