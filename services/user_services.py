from schemas.user_schema import UserAuth
from models.user_model import User
from core.security import get_password

class UserService:
  @staticmethod
  async def create_user(user: UserAuth):
    usuario = User(
      username = user.username,
      email = user.email,
      hash_password = get_password(user.password)
    )
    await user.save()
    return user
