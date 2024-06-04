from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Time, BLOB
from sqlalchemy.orm import relationship
from backend.data_access.base import Base

class Patient(Base):
    __tablename__ = 'patients'
    patientId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(20))
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

class Doctor(Base):
    __tablename__ = 'doctors'
    doctorId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    specialty = Column(String(255), nullable=False)

class LabTechnician(Base):
    __tablename__ = 'lab_technicians'
    technicianId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

class Appointment(Base):
    __tablename__ = 'appointments'
    appointmentId = Column(Integer, primary_key=True, autoincrement=True)
    patientId = Column(Integer, ForeignKey('patients.patient_id'))
    doctorId = Column(Integer, ForeignKey('doctors.doctor_id'))
    appointmentDate = Column(Date)
    appointmentTime = Column(Time)

class LabWork(Base):
    __tablename__ = 'lab_work'
    labWorkId = Column(Integer, primary_key=True, autoincrement=True)
    patientId = Column(Integer, ForeignKey('patients.patient_id'))
    technicianId = Column(Integer, ForeignKey('lab_technicians.technician_id'))
    testType = Column(String(255))
    testDate = Column(Date)
    testTime = Column(Time)

class TestResult(Base):
    __tablename__ = 'test_results'
    resultId = Column(Integer, primary_key=True, autoincrement=True)
    labWorkId = Column(Integer, ForeignKey('lab_work.labwork_id'))
    resultData = Column(BLOB)
    resultType = Column(String(50))

class Payment(Base):
    __tablename__ = 'payments'
    paymentId = Column(Integer, primary_key=True, autoincrement=True)
    patientId = Column(Integer, ForeignKey('patients.patient_id'))
    amount = Column(Float)
    paymentMethod = Column(String(255))
    paymentDate = Column(Date)
