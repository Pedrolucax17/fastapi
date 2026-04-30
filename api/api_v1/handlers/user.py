from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth
from services.user_services import UserService
import pymongo

user_router = APIRouter()

@user_router.post("/adiciona", summary="Adiciona usuario")
async def adiciona_usuario(data:UserAuth):
  try:
    return await UserService.create_user(data)
  except pymongo.error.DuplicateKeyError:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Username ou Email deste usuario ja existe"
    )