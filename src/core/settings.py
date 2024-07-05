from pydantic_settings import BaseSettings


class MongoSettings(BaseSettings):
    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_DB: str

    @property
    def MONGO_URI(self) -> str:
        return f"mongodb://{self.MONGO_USER}:{self.MONGO_PASSWORD}@{self.MONGO_HOST}:{self.MONGO_PORT}/"


class Settings(
    MongoSettings,
):
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
