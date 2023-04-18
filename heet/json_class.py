"""Класс для работы с Json-вакансии"""
import json
from heet.save import Save
import os


class JsonSave(Save):
    def __init__(self):
        self.file_name: str = 'JSON.json'