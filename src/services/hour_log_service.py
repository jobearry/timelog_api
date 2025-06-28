from src.repositories import hour_log_repository
from src.models.hour_log import HourLog

async def get_hour_log() -> HourLog:
  return await hour_log_repository.get_hour_log()