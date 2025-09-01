import logging
import os

from fastapi import Depends, FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api import ping, summaries
from app.config import Settings, get_settings
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )
    return application


app = create_application()
init_db(app)
