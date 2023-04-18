from abc import ABC, abstractmethod


class Save(ABC):

    @abstractmethod
    def results_json(self):
        pass
