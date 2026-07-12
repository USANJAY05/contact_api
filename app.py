from fastapi import FastAPI
from src.routes.contact import route as contact_route
from src.core.db import engine, Base
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    Base.metadata.create_all(bind=engine)

    yield

app = FastAPI(title="Contact API", lifespan=lifespan)

app.include_router(contact_route)

@app.get("/")
def home():
    return 'Welcome to contact API'