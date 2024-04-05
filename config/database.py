from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = "mongodb+srv://root:toor@onlinebackdb.xjwd4.mongodb.net/?retryWrites=true&w=majority&appName=OnlineBackdb"
client = MongoClient(MONGODB_URL)
db = client.students_db
students_collection = db.students

async_client = AsyncIOMotorClient(MONGODB_URL)
async_db = async_client.students_db
async_students_collection = async_db.students
