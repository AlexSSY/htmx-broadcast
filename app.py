import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from models import create_all_tables, seed


CURRENT_PATH = os.path.dirname(__file__)


@asynccontextmanager
async def liffespan(app: FastAPI):
    create_all_tables()
    seed()
    yield


app = FastAPI(lifespan=liffespan)
static_files = StaticFiles(directory=os.path.join(CURRENT_PATH, 'static'))
app.mount("/static", static_files, name="static")
