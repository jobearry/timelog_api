from beanie import Document
from datetime import datetime

class User(Document):
  username: str
  password: str
  email: str
  phone: str
  created_at: datetime
  is_active: bool
  role: str

  class Settings:
    name = "users"

