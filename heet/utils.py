from heet.hh_api import HeadHunterApi
from heet.json_class import JsonSave
from heet.supjob_api import SJAPI
from bs4 import BeautifulSoup


def user_interaction():
    """Общение-связь с пользователем"""
    hh_api, sj_api = choice_platform()
    hh_vacancies, sj_vacancies = get_from_platform(hh_api, sj_api)
    filter_word_input = filter_words()
    salary_input = salary_sort()
    get_result(hh_vacancies, sj_vacancies, filter_word_input, salary_input)


def choice_platform():
    """ Выбор платформы"""
    while True:
        platform = input('Выберите платформу: \n1 - hh.ru, \n2 - superjob.ru\n')
        if platform == '1':
            print('Вы выбрали платформу HeadHunter.ru')
            hh_api = HeadHunterApi()
            return hh_api, None
        elif platform == '2':
            print('Вы выбрали платформу Superjob.ru')
            sj_api = SJAPI()
            return None, sj_api
        else:
            print('Платформа не выбрана, попробуйте снова')
            continue


def get_from_platform(hh_api, sj_api):
    """Получение данных"""
    try:
        search_quere = input('Введите поисковый запрос: \n')
        if hh_api:
            hh_vacancies = hh_api.get_vacancies(search_quere)
            return hh_vacancies, None
        elif sj_api:
            sj_vacancies = sj_api.get_vacancies(search_quere)
            return None, sj_vacancies
        if hh_api and sj_api:
            hh_vacancies = hh_api.get_vacancies(search_quere)
            sj_vacancies = sj_api.get_vacancies(search_quere)
            return hh_vacancies, sj_vacancies
    except:
        print('Неверный запрос')


def filter_words():
    """Фильтрация вакансий по словам"""
    user_input = input('Введите ключевое слово для фильтрации данных: \n')
    return user_input


def remove_tags(text):
    """Удаляет тег"""
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text


def salary_sort():
    """Сортировка по заработной плате"""
    while True:
        salary_min = input('Введите минимальную заработную плату в рублях: \n')
        if not salary_min.strip():
            print('Неверный ввод')
            return '0'
        try:
            salary_min = int(salary_min)
            return salary_min
        except ValueError:
            print('Неверное значение')
            return '0'


def print_top_vacancies(final):
    """Вывод ТОП вакансий"""
    top = input('Введите количество вакансий: ')
    if top == '':
        top = len(final)
    else:
        top = int(top)
    if len(final) > 0:
        for i in range(min(top, len(final))):
            if final[i]['salary']['from'] == 0:
                salary_text = 'Заработная плата не указана'
            else:
                salary_text = f"Заработная плата: {final[i]['salary']['from']} рублей"
            print(
                f"{final[i]['title']} {salary_text} Описание вакансии: {remove_tags(final[i]['description'])} "
                f"Ссылка: {final[i]['url']}\n")
    else:
        print('Вакансий по запросу не найдено')


def get_result(hh_vacancies, sj_vacancies, filter_word_input, salary_input):
    """ Результат поиска"""
    json_save = JsonSave()
    json_save.save_file(headhunter=hh_vacancies, superjob=sj_vacancies)
    json_save.words_search(filter_word_input)
    json_save.get_vacancies_salary(salary_input)
    final = json_save.results_json()
    print_top_vacancies(final)
