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


