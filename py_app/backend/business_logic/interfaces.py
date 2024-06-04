from abc import ABC, abstractmethod

class IDataAccess(ABC):
    @abstractmethod
    def add_patient(self, patient):
        pass


class IReadFile(ABC):
    @abstractmethod
    def read(self, file_path):
        pass