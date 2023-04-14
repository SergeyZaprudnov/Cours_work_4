from abc import ABC, abstractmethod


class Save(ABC):

    @abstractmethod
    def dump_to_file(self, vacancy):
        pass
