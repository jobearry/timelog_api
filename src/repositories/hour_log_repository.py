from src.models.hour_log import HourLog

async def get_hour_log() -> HourLog:
  return await HourLog.find().to_list()