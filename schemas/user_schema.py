from pydantic import BaseModel, EmailStr, Field

class UserAuth(BaseModel):
  email: EmailStr = Field(..., description="Email user")
  username: str = Field(..., min_length=5, max_length=50, description="Username user")
  password: str = Field(..., min_length=5, max_length=20, description="Senha user")