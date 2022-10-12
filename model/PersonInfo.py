from sqlalchemy import Column, Text

from model.BaseModel import BaseModel


class PersonInfo(BaseModel):
    __tablename__ = 'person_info'

    surname = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    second_name = Column(Text)
    email = Column(Text)
    phone = Column(Text)

