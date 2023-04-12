"""Работа класса, для работы с ресурсом НН.ru"""
import requests
from heet.working_with_API import Working


class HeadHunterApi(Working):
    def __init__(self):
        self.vacancies = []

    def get_vacancies(self, search_query: str):
        """Правила запроса"""
        url = 'https://api.hh.ru/vacancies'
        params = {"text": search_query, "page": 10, "per_page": 100, "area": 113, "only_with_salary": True}

        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            vacancies = response.json()["items"]
            for vacancy in vacancies:
                self.vacancies.append(
                    {'name': vacancy['name'], 'url': vacancy['url'], 'description': vacancy['snippet']['requirement'],
                     'payment': vacancy['salary']})
                return self.vacancies
            else:
                return f'Error: {response.status_code}'
