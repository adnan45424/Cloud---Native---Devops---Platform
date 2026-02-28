import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "dev")
    app_name: str = os.getenv("APP_NAME", "platform-api")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()