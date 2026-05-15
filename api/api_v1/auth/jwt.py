from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any

from api.dependencies.user_deps import get_current_user
from models.user_model import User
from schemas.user_schema import UserDetail
from services.user_services import UserService
from core.security import create_refresh_token, create_access_token
from schemas.auth_schema import TokenSchema

auth_router = APIRouter()

@auth_router.post("/login", summary="Cria Access Token e Refresh Token", response_model=TokenSchema)
async def login(data: OAuth2PasswordRequestForm = Depends())-> Any:
  usuario = await UserService.authenticate(
    email=data.username,
    password=data.password
  )
  
  if not usuario:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Email ou senha estão incorretos"
    )
  return {
    "access_token": create_access_token(usuario.user_id),
    "refresh_token": create_refresh_token(usuario.user_id)
  }

@auth_router.post('/token-test', summary='Testando o Token', response_model=UserDetail)
async def test_token(user:User = Depends(get_current_user)):
  return user