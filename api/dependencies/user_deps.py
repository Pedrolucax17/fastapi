from fastapi.security import OAuth2AuthorizationCodeBearer
from core.config import settings
from fastapi import Depends, HTTPException, status
from models.user_model import User
from jose import jwt
from schemas.auth_schema import TokenPayload
from datetime import datetime
from pydantic import ValidationError
from services.user_services import UserService

oauth_reusavel = OAuth2AuthorizationCodeBearer(
  tokenUrl = f"{settings.API_V1_STR}/auth/login",
  scheme_name="JWT"
)

async def get_current_user(token:str = Depends(oauth_reusavel)) -> User:
  try:
    payload = jwt.decode(
      token=token,
      key=settings.JWT_SECRET_KEY,
      algorithms=settings.ALGORITHM_SECURITY 
    )
    token_data = TokenPayload(**payload)
    if datetime.fromtimestamp(token_data.exp) < datetime.now():
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token foi expirado",
        headers={'WWW-Authenticate': 'Bearer'}
      )
  except(jwt.JWTError, ValidationError):
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail='Erro na validação do token',
      headers={'WWW-Authenticate': 'Bearer'}
    )