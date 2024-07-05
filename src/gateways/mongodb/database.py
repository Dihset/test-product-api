from motor.motor_asyncio import AsyncIOMotorClient

from src.core.settings import settings


class Database:
    def __init__(self):
        self._client = AsyncIOMotorClient(settings.MONGO_URI)
        self._connection = self._client.get_database(settings.MONGO_DB)

    @property
    def connection(self):
        return self._connection
