from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from .database import db_manager


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    yield
    await db_manager.dispose()


app = FastAPI(lifespan=lifespan)
