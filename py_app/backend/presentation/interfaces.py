from abc import ABC, abstractmethod

class IPatientPresentation(ABC):
    @abstractmethod
    def register_patient(self):
        pass
