from typing import Annotated
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from apps.config import settings


class DBContextManager:
    def __init__(self, db_name):
        self.db_client = AsyncIOMotorClient(settings.DB_URL)
        self.db = self.db_client[db_name]
        self.todo_items = self.db['todo_items']
        self.todo_lists = self.db['todo_lists']
        self.users = self.db['users']

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.db_client.close()


async def get_db_context():
    with DBContextManager(settings.DB_NAME) as db_context:
        yield db_context

db_context = Annotated[DBContextManager, Depends(get_db_context)]
