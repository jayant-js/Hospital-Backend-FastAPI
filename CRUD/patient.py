from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import JSONResponse
from database import *
from models import *

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)

@router.post("/insert_new_patient")
def insert_patient(patient:Patient, session: Session = Depends(get_session)):
    patient.bmi = patient.weight/(patient.height**2)
    # insert this SQLModel patient into the database
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return JSONResponse(status_code=201, content="Patient Successfully Added")

@router.get("/get_patient_data/{patient_id}")
def get_patient_data(patient_id:int=Path(description="Give the Patient ID of the Patient", example=1), session:Session = Depends(get_session)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient.model_dump()