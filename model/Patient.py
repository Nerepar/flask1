from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

from model.BaseModel import BaseModel


class Patient(BaseModel):
    __tablename__ = 'patients'

    person_id = Column(Integer, ForeignKey('person_info.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    comment = Column(Text)
    date_birthday = Column(DateTime, nullable=False)
    date_in = Column(DateTime, nullable=False)
    date_out = Column(DateTime)

    person_info = relationship('Person_Info', lazy='join', foreign_keys=[person_id])
    doctor = relationship('Doctors', lazy='join', foreign_keys=[doctor_id])


