from fastapi import APIRouter, HTTPException
from src.models.user import User
from src.services import user_service

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

@router.get("/", response_model=list[User], summary="Retrieve a list of users")
async def get_users():
  try:
    return await user_service.get_users()
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))