from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from model.BaseModel import BaseModel


class Appointment_Service(BaseModel):
    __tablename__ = 'appointment_services'

    patient_id = Column(Integer, ForeignKey('patients.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    count = Column(Integer, nullable=False)
    date_appointments = Column(DateTime, nullable=False)
    date_complete = Column(DateTime)

    patient = relationship('Patients', lazy='join', foreign_keys=[patient_id])
    service = relationship('Services', lazy='join', foreign_keys=[service_id])
    doctor = relationship('Doctors', lazy='join', foreign_keys=[doctor_id])
