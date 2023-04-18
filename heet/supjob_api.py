"""Работа класса, для работы с ресурсом SupJob.ru"""
import os
import requests
from heet.working_with_API import Working
from heet.vacancies import Vacancy


class SJAPI(Working):
    def __init__(self):
        self.api_key: str = os.getenv('SJ_API_KEY')
        self.headers = {'X-Api-App-ID': self.api_key}
        self.url = 'https://api.superjob.ru/2.0/vacancies/'

