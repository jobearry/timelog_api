from beanie import Document
from pydantic import BaseModel
from datetime import datetime

class User(Document):
  user_id: int
  username: str
  password: str
  email: str
  phone: str
  created_at: datetime
  is_active: bool
  role: str

  class Settings:
    name = "users"

