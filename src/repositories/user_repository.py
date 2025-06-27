from src.models.user import User

async def get_users() -> User:
  return await User.find().to_list()