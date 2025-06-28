from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from src.models.user import User
from src.models.hour_log import HourLog
import os

load_dotenv()
async def init_db():
  url = os.getenv("DB_URI")
  client = AsyncIOMotorClient(url)
  db = client["timelog_dev"]

  await init_beanie(database=db, document_models=[User, HourLog])