from sqlmodel import SQLModel, Field
from typing import Annotated, Optional, List
from datetime import time
from pydantic import computed_field

class Patient(SQLModel, table=True):
    patient_id: Annotated[int, Field(..., primary_key=True, description="Provide the patient ID")]
    name: Annotated[str, Field(..., description="Please give the patient name")]
    age: Annotated[int, Field(..., description="Please provide the age of the patient", gt=0, le=120)]
    email: Annotated[Optional[str], Field(default=None, description="Please provide the patient's mail id")]
    contactNo: Annotated[str, Field(..., description="Please provide the patient's contact number", min_length=10, max_length=10)]
    height: Annotated[float, Field(..., description="Please give the patient's height in meters")]
    weight: Annotated[float, Field(..., description="Please give the patient's weight in Kgs")]

    @computed_field
    def bmi(self):
        return self.weight/(self.height*self.height)

class Doctor(SQLModel, table=True):
    doctor_id: Annotated[int, Field(..., primary_key=True,description="Please provide the doctor's ID")]
    name: Annotated[str, Field(..., description="Please give the doctor's name")]
    age: Annotated[int, Field(..., description="Please provide the age of the doctor", gt=0, le=120)]
    email: Annotated[Optional[str], Field(default=None, description="Please provide the doctor's mail id")]
    contactNo: Annotated[str, Field(..., description="Please provide the doctor's contact number", min_length=10, max_length=10)]

class Consultation(SQLModel, table=True):
    id: Annotated[Optional[int], Field(default=None)]
    patient_id: Annotated[int, Field(..., foreign_key="patient.patient_id")]
    doctor_id: Annotated[int, Field(..., foreign_key="doctor.doctor_id")]
    patientFeedback: Annotated[int, Field(..., description="Give the feedback about the doctor on the scale of 1-5", ge=0, le=5)]

class Specialization(SQLModel, table=True):
    specialization_id: Annotated[int, Field(..., primary_key=True)]
    specialization: Annotated[str, Field(..., description="Please specify the specialization")]

class DoctorSpecialization(SQLModel, table=True):
    doctor_id: Annotated[int, Field(..., foreign_key="doctor.doctor_id")]
    specialization_id: Annotated[int, Field(..., )]

class TimeSlot(SQLModel, table = True):
    timeslot_id: Annotated[int, Field(..., primary_key=True)]
    start_time: Annotated[time, Field(..., description="please provide the start time for the time slot")]
    end_time: Annotated[time, Field(..., description="please provide the end time for the time slot")]

class DoctorTimeSlot(SQLModel, table = True):
    doctor_id: Annotated[int, Field(..., foreign_key="doctor.doctor_id", description="Give the doctor id")]
    timeslot_id: Annotated[int, Field(..., foreign_key="timeslot.timeslot_id")]

