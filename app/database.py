from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    client: AsyncIOMotorClient = None
    
async def get_database() -> AsyncIOMotorClient:
    return Database.client[os.getenv("DB_NAME")]

async def connect_to_mongo():
    Database.client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
    
async def close_mongo_connection():
    Database.client.close()