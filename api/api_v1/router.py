from fastapi import APIRouter
from api.api_v1.handlers import user, todo
from api.api_v1.auth.jwt import auth_router

router = APIRouter()

router.include_router(
  user.user_router,
  prefix="/users",
  tags=['users']
)

router.include_router(
  auth_router,
  prefix='/auth',
  tags=['authi']
)

router.include_router(
  todo.todo_router,
  prefix='/todo',
  tags=['todo']
)