from fastapi import APIRouter, HTTPException
from src.models.hour_log import HourLog
from src.services import hour_log_service

router = APIRouter(prefix="/api/v1/hour-log", tags=["Manhour Logs"])

@router.get("/", response_model=list[HourLog], summary="Retrieve a list of users manhour logs")
async def get_users():
  try:
    return await hour_log_service.get_hour_log()
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))