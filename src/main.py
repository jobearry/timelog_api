from fastapi import FastAPI
from src.controllers.user_controller import router as user_router
from src.db import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title="Timelog API: Dev",
    lifespan=lifespan
) 

app.include_router(user_router)