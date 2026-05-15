from fastapi import APIRouter

todo_router = APIRouter()

@todo_router.get("/test")
async def test():
    return 'test'