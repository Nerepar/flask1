from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship

from model.BaseModel import BaseModel


class Accrual(BaseModel):
    __tablename__ = 'accruals'

    patients_id = Column(Integer, ForeignKey('patients.id'))
    sum = Column(DECIMAL, default=0)
    date = Column(DateTime, nullable=False)

    patient = relationship('Patients', lazy='join', foreign_keys=[patients_id])