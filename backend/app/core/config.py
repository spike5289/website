"""
Configuration settings for the FastAPI application
"""
import os
from typing import List
from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application settings"""
    
    # App settings
    app_name: str = "AI Consulting API"
    app_version: str = "1.0.0"
    environment: str = os.getenv("ENVIRONMENT", "development")
    
    # CORS settings
    allowed_origins: List[str] = [
        "http://localhost:3000",
        "https://your-frontend-app.herokuapp.com"
    ]
    
    # API settings
    api_prefix: str = "/api"
    
    class Config:
        env_file = ".env"

settings = Settings()
