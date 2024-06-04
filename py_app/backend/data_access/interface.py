from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def read(self, file_path):
        pass
