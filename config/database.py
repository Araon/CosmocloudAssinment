from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URL = os.getenv("MONGODB_URL") + "=true&w=majority"


async_client = AsyncIOMotorClient(MONGODB_URL)
async_db = async_client.students_db
async_students_collection = async_db.students
