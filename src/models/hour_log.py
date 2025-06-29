from typing import List
from beanie import Document, PydanticObjectId
from datetime import datetime

from pydantic import BaseModel

class ManhourEntry(BaseModel):
  project_name: str
  task_name: str
  task_description: str
  hour_input: int
  
class HourLog(Document):
  user_id: PydanticObjectId | None
  manhour_info: List[ManhourEntry]
  input_date: datetime

  class Settings:
    name = "hour_logs"
  