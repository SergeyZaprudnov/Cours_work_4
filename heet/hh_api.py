"""Работа класса, для работы с ресурсом НН.ru"""
import requests
from heet.working_with_API import Working


class HeadHunterApi(Working):
    def __init__(self):
        self.vacancies = []
