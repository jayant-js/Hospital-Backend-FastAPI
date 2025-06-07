from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from database import *
from CRUD import *
from CRUD import __all__

app = FastAPI()
for router_name in __all__:
    app.include_router(globals()[router_name])

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables() 
    yield

@app.get("/")
def introduction_page():
    return {"message":"this is a backend project for patients database for a hospital"}