"""Работа класса, для работы с ресурсом НН.ru"""
import requests
from heet.working_with_API import Working
from heet.vacancies import Vacancy


class HeadHunterApi(Working):
    def __init__(self):
        self.url_hh = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query):
        """Правила запроса"""
        params = {'text': search_query, 'per_page': 100, 'area': 113}
        response = requests.get(self.url_hh, params=params)
        if response.status_code == 200:
            data = response.json()
            vacancies_data = data['items']
            vacancies = []
            for vacancy in vacancies_data:
                title = vacancy['name']
                salary = HeadHunterApi.get_salary(vacancy['salary'])
                description = vacancy['snippet']['requirement']
                url = vacancy['alternate_url']
                vacancy = Vacancy(title, salary, description, url)
                vacancies.append(vacancy)
            return vacancies
        else:
            return f'Error: {response.status_code}'

    @staticmethod
    def get_salary(salary_data, **kwargs):
        if salary_data is None:
            salary = {'from': 0, 'currency': 'RUR'}
        elif 'to' not in salary_data or salary_data['to'] is None:
            salary = {'from': salary_data.get('from', 0), 'currency': salary_data.get('currency', 'RUR')}
        elif 'from' not in salary_data or salary_data['from'] is None:
            salary = {'from': salary_data['to'], 'currency': salary_data.get('currency', 'RUR')}
        else:
            salary = {'from': salary_data['from'], 'to': salary_data['to'],
                      'currency': salary_data.get('currency', 'RUR')}
        return salary
