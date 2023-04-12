"""Класс для работы с вакансиями"""


class Vacancy:
    __slots__ = ('__name', '__url', '__description', '__payment')

    def __init__(self, name: str, url: str, description: str, payment: str):
        self.__name = name
        self.__url = url
        self.__description = description
        self.__payment = payment

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url
