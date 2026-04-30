from schemas.user_schema import UserAuth
from models.user_model import User

class UserService:
  @staticmethod
  async def create_user(user: UserAuth):
    usuario = User(
      username = user.username,
      email = user.email,
      hash_password = user.password
    )
