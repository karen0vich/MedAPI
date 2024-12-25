from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"
    
    patient_id = Column(Integer, primary_key=True, index=True)
    fio = Column(String(255), index=True)
    year_of_birth = Column(Integer)
    social_status = Column(String(255))
    medical_history = Column(JSON)  # JSON field for requirement 6
    
    treatments = relationship("Treatment", back_populates="patient")

class Doctor(Base):
    __tablename__ = "doctors"
    
    doctor_id = Column(Integer, primary_key=True, index=True)
    fio = Column(String(255), index=True)
    specialization = Column(String(255))
    experience = Column(Integer)
    
    treatments = relationship("Treatment", back_populates="doctor")

class Treatment(Base):
    __tablename__ = "treatments"
    
    treatment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id"))
    diagnosis = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    current_condition = Column(String(255))
    
    patient = relationship("Patient", back_populates="treatments")
    doctor = relationship("Doctor", back_populates="treatments")
