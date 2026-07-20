from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "TalentFlow AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    GEMINI_API_KEY: str

    GEMINI_MODEL: str = "gemini-3.5-flash"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()




## old version
# from dotenv import load_dotenv
# import os

# load_dotenv()


# class Settings:
#     APP_NAME = os.getenv("APP_NAME", "TalentFlow AI")
#     APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
#     DEBUG = os.getenv("DEBUG", "False").lower() == "true"

#     GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# settings = Settings()