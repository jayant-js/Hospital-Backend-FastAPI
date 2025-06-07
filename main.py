from fastapi import FastAPI, HTTPException, Path, Query, Depends, APIRouter
from CRUD import *
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from sqlmodel import Field, SQLModel, create_engine, select
from database import *

app = FastAPI()
app.include_router(patient_router)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables() 
    yield

@app.get("/introduction")
def introduction_page():
    return {"message":"this is a backend project for patients database for a hospital"}