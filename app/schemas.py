from pydantic import BaseModel
from datetime import date
from typing import Optional

class PatientBase(BaseModel):
    fio: str
    year_of_birth: int
    social_status: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    patient_id: int
    
    class Config:
        orm_mode = True

class DoctorBase(BaseModel):
    fio: str
    specialization: str
    experience: int

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    doctor_id: int
    
    class Config:
        orm_mode = True

class TreatmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    diagnosis: str
    start_date: date
    end_date: Optional[date] = None
    current_condition: Optional[str] = None

class TreatmentCreate(TreatmentBase):
    pass

class Treatment(TreatmentBase):
    treatment_id: int
    
    class Config:
        orm_mode = True
