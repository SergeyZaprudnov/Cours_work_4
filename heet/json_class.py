"""Класс для работы с Json-вакансии"""
import json
from heet.save import Save
import os


class JsonSave(Save):
    def __init__(self):
        self.file_name: str = 'JSON.json'

    def save_file(self, headhunter=None, superjob=None):
        """Сохранение данных с вакансиями"""
        if headhunter is not None and superjob is None:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump(
                    sorted([vars(vacancy) for vacancy in headhunter], key=lambda x: x['salary']['from'], reverse=True),
                    file, ensure_ascii=False, indent=4)
        elif superjob is not None and headhunter is None:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump(
                    sorted([vars(vacancy) for vacancy in superjob], key=lambda x: x['salary']['from'], reverse=True),
                    file, ensure_ascii=False, indent=4)
        else:
            print('Нет вакансий')

