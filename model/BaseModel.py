import datetime
from typing import List

from sqlalchemy import Column, Integer, DateTime

from app import Model, engine
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class BaseModel(Model):
    __abstract__ = True
    session = engine.session

    _guarded: List[str] = []
    _fillable: List[str] = []
    _manual_fillable: List[str] = []

    id = Column(Integer, primary_key=True)

    crated_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullabble=True)

    def from_object(self, record: dict):
        """
        Создание модели из словаря

        :param record: Запись  - словарь с данными
        """

        fields = self._get_fillable_fields()

        for field in fields:
            if field in record:
                setattr(self, field, record.get(field))

        if not self.crated_at:
            self.crated_at = datetime.datetime.now()
        else:
            self.updated_at = datetime.datetime.now()

        self._manual_fillable_fields(record)

        return self

    def to_dict(self) -> dict:
        """
        Преобразование модели в словарь
        :return: Словарь с данными из модели
        """

        result = {}

        columns = self._get_columns()

        for column_name in columns:
            result[column_name] = getattr(self, column_name)

        self._manual_response_fields(result)

        return result

    def add_default_data(self):
        """Добавление начальных данных"""
        pass

    def _manual_fillable_fields(self, record: dict):
        """
        Ручное заполнение модели перед сохранением
        """
        pass

    def _manual_response_fields(self, result: dict):
        """Заполнение полей перед ответом"""
        pass

    def _get_columns(self) -> List[str]:
        """
        Получение списка колонок, которые возвращаются из модели
        :return: список колонок для метода to_dict
        """
        return self._get_columns_name(self._guarded)

    def _get_fillable_fields(self) -> List[str]:
        """
        Получение списка полей для заполнения
        """
        return self._get_columns_name(self._manual_fillable)

    def _get_columns_name(self, skip_fields: List[str]) -> List[str]:
        """
        Получение полей, которые не содержаться в функции skip_fields
        :param skip_fields: Пропускание поля
        """
        columns = self.metadata.tables.get(self.__tablename__).columns

        if columns:
            return [column_name for column_name in columns if column_name not in skip_fields]

        return []
