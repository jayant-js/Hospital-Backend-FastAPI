from fastapi import FastAPI, HTTPException, Path, Query, Depends
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel
from typing import Annotated
import pymysql
from models import *

app = FastAPI()

URL_DATABASE = 'mysql+pymysql://root:abhi@localhost:3306/hospital_db'
engine = create_engine(URL_DATABASE, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables() 
    yield

@app.get("/introduction")
def introduction_page():
    return {"message":"this is a backend project for patients database for a hospital"}

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/get_patient_data/{patient_id}")
def get_patient_data(patient_id:int=Path(description="Give the Patient ID of the Patient", example=1), session:Session = Depends(get_session)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient.model_dump()

@app.post("/insert_new_patient")
def insert_patient(patient:Patient, session: Session = Depends(get_session)):
    patient.bmi = patient.weight/(patient.height**2)
    # insert this SQLModel patient into the database
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return JSONResponse(status_code=201, content="Patient Successfully Added")