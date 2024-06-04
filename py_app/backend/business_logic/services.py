#from backend.business_logic.interfaces import IDataAccess
from backend.data_access.repository import Repository
from backend.data_access.models import Patient, Doctor, LabTechnician, Appointment, LabWork, TestResult, Payment

from backend.data_access.repository import read_data_from_csv

#class PatientService:
#    def __init__(self, data_access: IDataAccess):
#        self.data_access = data_access

#    def register_patient(self, name, email, password):
#        new_patient = Patient(name=name, email=email, password=password)
#        self.data_access.add_patient(new_patient)

class PatientService:
    def __init__(self):
        self.repo = Repository() #instance
    
    def get_patient_data(self, patient):
        return self.repo.get_patient_by_email(patient.email)

class CSVReader():
    def __init__(self):
        self.df = None #data from file variable
        self.repo = Repository() #instance

    def read(self, file_path):
        
        self.df = read_data_from_csv(file_path)
    
    def write_to_database(self):
        for index, row in self.df.iterrows():
            entity_type = row[0]
            data = row[1:].tolist()  # Отримуємо дані без назви сутності

            if entity_type == 'Patients':
                self.repo.add_patient(name=data[0], phone=data[1], email=data[2], password=data[3])
            elif entity_type == 'Doctors':
                self.repo.add_doctor(name=data[0], specialty=data[1])
            elif entity_type == 'LabTechnicians':
                self.repo.add_lab_technician(name=data[0])
            elif entity_type == 'Appointments':
                self.repo.add_appointment(patient_id=data[0], doctor_id=data[1], date=data[2], time=data[3])
            elif entity_type == 'LabWork':
                self.repo.add_lab_work(patient_id=data[0], technician_id=data[1], test_type=data[2], test_date=data[3], test_time=data[4])
            elif entity_type == 'TestResults':
                self.repo.add_test_result(lab_work_id=data[0], result_data=data[1], result_type=data[2])
            elif entity_type == 'Payments':
                self.repo.add_payment(patient_id=data[0], amount=data[1], payment_method=data[2], payment_date=data[3])

            print(f"Added {entity_type} record: {data}")

            print("CSV file has been processed successfully.")