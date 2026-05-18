from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from models.user_model import User
from models.todo_model import Todo
from services.todo_service import TodoService
from schemas.todo_schema import TodoDetail, TodoCreate
from api.dependencies.user_deps import get_current_user

todo_router = APIRouter()

@todo_router.get("/", summary="Lista todas as rotas", response_model=List[TodoDetail])
async def list_todo(current_user:User = Depends(get_current_user)):
    return await TodoService.list_todos(current_user)

@todo_router.post("/create", summary="Adicionando Nota",response_model=Todo)
async def create_todo(data: TodoCreate, current_user:User = Depends(get_current_user)):
    return await TodoService.create_todo(current_user, data)

@todo_router.get("/{todo_id}", summary="Detalhe de nota por id", response_model=TodoDetail)
async def detail(todo_id: UUID, current_user:User = Depends(get_current_user)):
    return await TodoService.detail(current_user, todo_id)