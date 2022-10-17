from classes.BaseClass import BaseClass
from model.PersonInfo import PersonInfo as PersonInfoModel


class PersonInfo(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False) -> PersonInfoModel:
        return PersonInfoModel() if new_model else PersonInfoModel

