from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID

class UserAuth(BaseModel):
  email: EmailStr = Field(..., description="Email user")
  username: str = Field(..., min_length=5, max_length=50, description="Username user")
  password: str = Field(..., min_length=5, max_length=20, description="Senha user")

class UserDetail(BaseModel):
  user_id: UUID
  username: str
  email: EmailStr
  first_name: Optional[str] = None
  last_name: Optional[str] = None
  disabled: Optional[bool] = None