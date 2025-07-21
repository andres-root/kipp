from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the application"""

    # Environment
    environment: str = "local"  # local, dev, qa, staging, prod

    # Database settings
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_password: str
    db_connection_string: str = ""

    # OpenAI settings
    openai_api_key: str

    # Anthropic settings
    anthropic_api_key: str

    # Langsmith settings
    langsmith_tracing: bool
    langsmith_endpoint: str
    langsmith_api_key: str
    langsmith_project: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings()
