from heet.hh_api import HeadHunterApi
from heet.json_class import JsonSave
from heet.supjob_api import SJAPI
from  bs4 import BeautifulSoup



def get_search_query():
    query = input("Введите запрос: ")
    return query
