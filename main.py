from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
  client_db = AsyncIOMotorClient(
    settings.MONGO_CONNECTION_STRING
  ).todoapp
  
  await init_beanie(
    database=client_db,
    document_models= []
  )

app = FastAPI(
  title=settings.PROJECT_NAME,
  openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


