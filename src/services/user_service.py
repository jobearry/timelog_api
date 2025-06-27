from src.repositories import user_repository
from src.models.user import User

async def get_users() -> User:
  return await user_repository.get_users()