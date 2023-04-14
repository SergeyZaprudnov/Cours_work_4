"""Класс для работы с Json-вакансии"""
import json
from heet.hh_api import HeadHunterApi
from heet.save import Save


class JsonSave(Save):
    def __init__(self, filename):
        self.filename = filename
        self.vacancies = []

    def dump_to_file(self, **kwargs):
        with open("data.json", "w", encoding='utf - 8') as outfile:
            json.dump(self.filename, outfile, indent=1, ensure_ascii=False)
