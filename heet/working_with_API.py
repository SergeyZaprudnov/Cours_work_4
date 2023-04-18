"""Абстрактный класс для работы с API"""

from abc import ABC, abstractmethod


class Working(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass

    @staticmethod
    def get_pay(self, pay_data):
        pass
