from beanie import Document
from pydantic import BaseModel
from datetime import datetime

class HourLog(Document):
  log_id: int
  user_id: int
  hour_entry: int
  input_date: datetime

  class Settings:
    name = "hour_logs"