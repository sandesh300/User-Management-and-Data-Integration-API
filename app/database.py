# remote-brick/database.py
from pymongo import MongoClient
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB connection
try:
    client = MongoClient(
        "mongodb+srv://instagramloginn1:b9b32wz1hY6MrzZ1@remotebrick.vic3l.mongodb.net/?retryWrites=true&w=majority&appName=remoteBrick",
    )
    db = client.mydatabase
    logger.info("Connected to MongoDB")
except Exception as e:
    logger.error(f"Error connecting to MongoDB: {e}")

def get_user_collection():
    return db.users

def get_details_collection():
    return db.details
