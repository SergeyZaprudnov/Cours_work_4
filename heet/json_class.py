"""Класс для работы с Json-вакансии"""
import json
from heet.hh_api import HeadHunterApi
from heet.save import Save

class JsonSave(Save):
    def __init__(self, filename):
        self.filename = filename
        self.vacancies = []