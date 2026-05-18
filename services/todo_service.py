from models.user_model import User
from models.todo_model import Todo
from typing import List
from schemas.todo_schema import TodoCreate

class TodoService:
    @staticmethod
    async def list_todos(user: User) -> List[Todo]:
        todos = await Todo.find(Todo.owner.id == user.id).to_list()
        return todos

    @staticmethod
    async def create_todo(user: User, data: TodoCreate) -> Todo:
        todo = Todo(**data.model_dump(), owner=user)
        return await todo.insert()