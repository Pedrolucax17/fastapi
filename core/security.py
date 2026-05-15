import hashlib
from passlib.context import CryptContext
from typing import Union, Any
from datetime import datetime, timedelta, timezone
from jose import jwt 
from core.config import settings

password_context = CryptContext(
  schemes=["bcrypt"],
  deprecated="auto"
)

def _normalize_password(password: str) -> str:
  return hashlib.sha256(password.encode("utf-8")).hexdigest()

def get_password(password: str) -> str:
  normalized = _normalize_password(password)
  return password_context.hash(normalized)

def verify_password(password: str, hashed_password: str) -> bool:
  normalized = _normalize_password(password)
  return password_context.verify(normalized, hashed_password)

def create_access_token(subject:Union[str, Any], expires_delta:int=None)->str:
  if expires_delta is not None:
    expires_delta = datetime.now(timezone.utc) + expires_delta
  else:
    expires_delta = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
  
  info_jwt = {
    "exp": expires_delta,
    "sub": str(subject)
  }
  
  jwt_encoded = jwt.encode(
    info_jwt,
    settings.JWT_SECRET_KEY,
    settings.ALGORITHM_SECURITY
  )
  
  return jwt_encoded
    
def create_refresh_token(subject:Union[str, Any], expires_delta:int=None)->str:
  if expires_delta is not None:
    expires_delta = datetime.now(timezone.utc) + expires_delta
  else:
    expires_delta = datetime.now(timezone.utc) + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
  
  info_jwt = {
    "exp": expires_delta,
    "sub": str(subject)
  }
  
  jwt_encoded = jwt.encode(
    info_jwt,
    settings.JWT_REFRESH_SECRET_KEY,
    settings.ALGORITHM_SECURITY
  )
  
  return jwt_encoded
    