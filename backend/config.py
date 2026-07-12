import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "dev-jwt-secret-change-in-production")
    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/2ksolutions",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    JWT_ACCESS_TOKEN_EXPIRES: int = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", "3600"))
    JWT_REFRESH_TOKEN_EXPIRES: int = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", "2592000"))
    RATELIMIT_DEFAULT: str = os.getenv("RATELIMIT_DEFAULT", "100/hour")
    RATELIMIT_STORAGE_URI: str = os.getenv("RATELIMIT_STORAGE_URI", "memory://")
    CORS_ORIGINS: list[str] = os.getenv("CORS_ORIGINS", "http://localhost:5000").split(",")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    JWT_TOKEN_LOCATION: list[str] = ["headers"]
    JWT_ACCESS_COOKIE_NAME: str = "access_token_cookie"
    JWT_REFRESH_COOKIE_NAME: str = "refresh_token_cookie"
    JWT_COOKIE_CSRF_PROTECT: bool = False


class TestConfig(Config):
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///:memory:"
    RATELIMIT_ENABLED: bool = False
