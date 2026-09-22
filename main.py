from fastapi import Depends, FastAPI, status
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import engine, get_setting
from app.models.base import Base
from app.api.routers.task import router as task_router
from app.api.routers.category import router as category_router




@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

settings = get_setting()
app = FastAPI(lifespan=lifespan)
app.include_router(task_router, tags=['tasks']),
app.include_router(category_router, tags=['category']),
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allow_origins_url,
    allow_methods=["*"],
)













    