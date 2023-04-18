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

    def get_vacancies_salary(self, salary_input):
        """Список вакансий с заданной заработной платой"""
        with open(self.file_name, 'r', encoding='utf-8') as file:
            vacancy = json.load(file)

        vacancy_dict = []

        try:
            salary, currency = salary_input.split(' ')
        except:
            salary = salary_input
            currency = ['руб', 'rur', 'RUR', 'rub']

        if currency in ['руб', 'RUR', 'rub']:
            currency = ['руб', 'rur', 'RUR', 'rub']

        for i in vacancy:
            try:
                if int(i['salary']['from']) >= int(salary) and i['salary']['cerrency'] in currency:
                    vacancy_dict.append(i)
                elif i['salary']['currency'] in ['USD', 'usd'] and int(i['salary']['from']) * 83 >= int(salary):
                    vacancy_dict.append(i)
            except:
                continue

        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(vacancy_dict, file, ensure_ascii=False, indent=4)

    def words_search(self, words_search):
        """Поиск по словам"""
        if not isinstance(words_search, str):
            return "Error: запрос не строка"
        if words_search == '':
            with open(self.file_name, 'r', encoding='utf-8') as file:
                vacancies = json.load(file)
            return vacancies
        else:
            with open(self.file_name, 'r', encoding='utf -8') as file:
                vacancies = json.load(file)
            result = []
            for vacancy in vacancies:
                for words in words_search.split():
                    if words.lower() in vacancy['description'].lower():
                        result.append(vacancy)
                        break
                    return result

    def results_json(self):
        """Итог"""
        with open(self.file_name, 'r', encoding='utf-8') as file:
            fin_result = json.load(file)
        return fin_result
