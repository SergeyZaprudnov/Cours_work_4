from abc import ABC, abstractmethod


class Save(ABC):

    @abstractmethod
    def results_json(self):
        pass

    @staticmethod
    def words_search(self, words_search):
        pass

    @staticmethod
    def get_vacancies_salary(self, salary_input):
        pass

    @staticmethod
    def save_file(self, resourse=None):
        pass
