from sqlalchemy.orm import Session

from app import engine
from helpers.HttpResponse import HttpResponse
from model.BaseModel import BaseModel


class BaseClass:
    USE_NAVIGATION: bool = True
    FIELD_SORT: str = None
    AREA: str = 'BaseClass'

    _session: Session = engine.session
    _additional_methods: dict = None

    def __init__(self):
        self._methods_map = {
            'Create': self.create,
            'Get': self.get,
            'Delete': self.delete,
            'Update': self.update,
            'List': self.list
        }

        if self._additional_methods:
            self._methods_map.update(self._additional_methods)

    @staticmethod
    def get_model(new_model: bool = False) -> BaseModel:
        """
        Получение модели

        :param new_model: Признак создавать экземпляр или нет
        :return: Модель сущности
        """
        return BaseModel() if new_model else BaseModel

    def get(self, **kwargs):
        """
        Меод получения записи по ключу

        :param kwargs: В data содержится ключ записи
        :return: Запись или ошибку, если ее нет
        """
        key = kwargs.get('data')
        query = self._session.query(self.get_model()).get(key)

        if query:
            return HttpResponse.make(data=query.to_dict())
        else:
            return HttpResponse.make(
                success=False,
                error_text=f'Запись в таблице (self.get_model(True).__tablename__) '
                           f'по ключу (key) не найдена'
            )
