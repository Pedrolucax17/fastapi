from typing import List
from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.todo_schema import TodoDetail
from api.dependencies.user_deps import get_current_user

todo_router = APIRouter()

@todo_router.get("/", summary="Lista todas as rotas", response_model=List[TodoDetail])
async def list(current_user:User = Depends(get_current_user)):
    pass