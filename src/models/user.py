from pydantic import BaseModel
from datetime import datetime

class UserResponse(BaseModel):
  id: int
  username: str
  password: str
  email: str
  phone: str
  created_at: datetime
  is_active: bool
  role: str

  class Config:
    allow_population_by_field_name = True