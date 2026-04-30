from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from models.user_model import User
from api.api_v1.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
  client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
  
  db = client["todoapp"]
  
  await init_beanie(
    database=db,
    document_models= [
      User
    ]
  )
  
  print("Conexão com MongoDB (Beanie) inicializada!")

  yield 
  
  client.close()
  print("Conexão com MongoDB encerrada.")

app = FastAPI(
  title=settings.PROJECT_NAME,
  openapi_url=f"{settings.API_V1_STR}/openapi.json",
  lifespan=lifespan
)

app.include_router(
  router,
  prefix=settings.API_V1_STR
)


