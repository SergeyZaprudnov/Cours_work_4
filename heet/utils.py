from heet.hh_api import HeadHunterApi
from heet.json_class import JsonSave
from heet.supjob_api import SJAPI
from  bs4 import BeautifulSoup



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
            print('Вы выбрали платформу Superjob.ru' )
            sj_api = SJAPI()
            return sj_api, None
        else:
            print('Платформа не выбрана, попробуйте снова')
            continue

