from fastapi import APIRouter, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from sqlmodel import select
from database import *
from models import *

router = APIRouter(
    prefix="/doctors",
    tags=["Doctor"]
)

@router.post("/new_doctor")
def new_doctor(doctor: Doctor, session: Session=Depends(get_session)):
    session.add(doctor)
    session.commit()
    session.refresh(doctor)
    return JSONResponse(status_code=201, content="Doctor has been successfully added")

@router.get("/get_all_doctors")
def get_doctors_list(session: Session = Depends(get_session)):
    statement = select(Doctor)
    return session.exec(statement).all()
    
# @router.get("/get_doctor")
# def get_doctor(
#     name:str = Query(), 
#     doctor_id:int = Query(), 
#     session: Session=Depends(get_session)):
