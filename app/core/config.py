from pydantic import BaseModel
import os

class Settings(BaseModel):
    app_name: str = "Demo API"
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    version: str = os.getenv("VERSION", "1.0.0")

settings = Settings()
