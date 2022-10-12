from sqlalchemy import Column, Integer, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship

from model.BaseModel import BaseModel


class Doctor(BaseModel):
    __tablename__ = 'doctors'

    person_id = Column(Integer, ForeignKey('person_info.id'))
    position = Column(Text)
    is_active = Column(Boolean, default=True)

    person_info = relationship('Person_Info', lazy='join', foreign_keys=[person_id])
