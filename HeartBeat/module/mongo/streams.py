from typing import Dict, List, Union
from motor.motor_asyncio import AsyncIOMotorClient
import config

# Initialize MongoDB directly from config
try:
    _mongo_async_ = AsyncIOMotorClient(config.MONGO_URL)
    mongodb = _mongo_async_.Genius   # Use the same DB name as before
    streamsdb = mongodb.streamsdb
except Exception as e:
    print(f"MongoDB Connection Error: {e}")
    raise e


async def get_chat_id(user_id: int) -> int:
    check = await streamsdb.find_one(
        {"user_id": user_id, "chat_id": {"$lt": 0}}
    )
    if not check:
        return 0
    return check["chat_id"]


async def is_chat_id(user_id: int, chat_id: int) -> bool:
    is_chat = await get_chat_id(user_id)
    return chat_id == is_chat


async def set_chat_id(user_id: int, chat_id: int) -> bool:
    if await is_chat_id(user_id, chat_id):
        return True
    get_chat = await get_chat_id(user_id)
    await streamsdb.update_one(
        {"user_id": user_id, "chat_id": get_chat},
        {"$set": {"user_id": user_id, "chat_id": chat_id}},
        upsert=True,
    )
    return False
