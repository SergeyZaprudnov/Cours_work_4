from heet.hh_api import HeadHunterApi
from heet.json_class import JsonSave
from heet.supjob_api import SJAPI
from bs4 import BeautifulSoup


def user_interaction():
    """Общение\связь с пользователем"""
    hh_api, sj_appi = choice_platform()
    hh_vacancies, sj_vacancies = get_from_platform
    filter_word_input = filter_words()
    salary_input = salary_sort()
    get_result(hh_vacancies, sj_vacancies, filter_word_input, salary_input)


def choise_platform():
    """ Выбор платформы"""
    while True:
        platform = input('Выбор платфоры (hh.ru 1, superjob.ru 2:')
        if platform == '1':
            print('Вы выбрали платформу HeadHunter.ru')
            hh_api = HeadHunterApi()
            return hh_api, None
        elif platform == '2':
            print('Вы выбрали платформу Superjob.ru')
            sj_api = SJAPI()
            return sj_api, None
        else:
            print('Платформа не выбрана, попробуйте снова')
            continue


def get_from_platfom(hh_api, sj_api):
    """Получение данных"""
    try:
        search_quere = input('Введите запрос: ')
        if hh_api:
            hh_vacancies = hh_api.get_vacancies(search_quere)
            return hh_vacancies, None
        elif sj_api:
            sj_vacancies = sj_api.get_vacancies(search_quere)
            return sj_vacancies, None
        if hh_api and sj_api:
            hh_vacancies = hh_api.get_vacancies(search_quere)
            sj_vacancies = sj_api.get_vacancies(search_quere)
            return hh_vacancies, sj_vacancies
    except:
        print('Неверный запрос')

def filter_words():
    """Фильтрация вакансий по словам"""
    user_input = input('ВВедите ключевое слово: \n')
    return user_input

def remove_tags(text):
    """Удаляет тег"""
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text

