from sqlalchemy.orm import sessionmaker
from backend.data_access.database import DatabaseManager
from backend.data_access.models import Patient, Doctor, LabTechnician, Appointment, LabWork, TestResult, Payment
import pandas as pd


def read_data_from_csv(file_path):
           df = pd.read_csv(file_path, header=None)  # Читання CSV без заголовків
           return df

class Repository:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.Session = sessionmaker(bind=self.db_manager.engine)

    def add_entity(self, entity):
        session = self.db_manager.create_session()
        try:
            session.add(entity)
            session.commit()
            print(f"{entity.__class__.__name__} added successfully.")
        except Exception as e:
            session.rollback()
            print(f"Failed to add {entity.__class__.__name__}: {str(e)}")
        finally:
            self.db_manager.close_session(session)

    def get_all_entities(self, entity_class):
        session = self.db_manager.create_session()
        try:
            entities = session.query(entity_class).all()
            return entities
        except Exception as e:
            print(f"Failed to fetch entities: {str(e)}")
            return []
        finally:
            self.db_manager.close_session(session)

    def add_patient(self, **kwargs):
        self.add_entity(Patient(**kwargs))

    def get_patient_by_email(self, email):
        session = self.db_manager.create_session()
        try:
            # Виконання запиту до бази даних за email
            patient = session.query(Patient).filter(Patient.email == email).first()
            return patient
        except Exception as e:
            print(f"Failed to fetch patient: {str(e)}")
            return None
        finally:
            self.db_manager.close_session(session)

    def get_all_patients(self):
        return self.get_all_entities(Patient)

    def add_doctor(self, **kwargs):
        self.add_entity(Doctor(**kwargs))

    def get_all_doctors(self):
        return self.get_all_entities(Doctor)

    def add_lab_technician(self, **kwargs):
        self.add_entity(LabTechnician(**kwargs))

    def get_all_lab_technicians(self):
        return self.get_all_entities(LabTechnician)

    def add_appointment(self, **kwargs):
        self.add_entity(Appointment(**kwargs))

    def get_all_appointments(self):
        return self.get_all_entities(Appointment)

    def add_lab_work(self, **kwargs):
        self.add_entity(LabWork(**kwargs))

    def get_all_lab_work(self):
        return self.get_all_entities(LabWork)

    def add_test_result(self, **kwargs):
        self.add_entity(TestResult(**kwargs))

    def get_all_test_results(self):
        return self.get_all_entities(TestResult)

    def add_payment(self, **kwargs):
        self.add_entity(Payment(**kwargs))

    def get_all_payments(self):
        return self.get_all_entities(Payment)
    
    def import_data_from_csv(self, file_path):
        df = pd.read_csv(file_path, header=None)  # Читання CSV без заголовків
        for index, row in df.iterrows():
            entity_type = row[0]
            data = row[1:].tolist()  # Отримуємо дані без назви сутності

            if entity_type == 'Patients':
                self.add_patient(name=data[0], phone=data[1], email=data[2], password=data[3])
            elif entity_type == 'Doctors':
                self.add_doctor(name=data[0], specialty=data[1])
            elif entity_type == 'LabTechnicians':
                self.add_lab_technician(name=data[0])
            elif entity_type == 'Appointments':
                self.add_appointment(patient_id=data[0], doctor_id=data[1], date=data[2], time=data[3])
            elif entity_type == 'LabWork':
                self.add_lab_work(patient_id=data[0], technician_id=data[1], test_type=data[2], test_date=data[3], test_time=data[4])
            elif entity_type == 'TestResults':
                self.add_test_result(lab_work_id=data[0], result_data=data[1], result_type=data[2])
            elif entity_type == 'Payments':
                self.add_payment(patient_id=data[0], amount=data[1], payment_method=data[2], payment_date=data[3])

            print(f"Added {entity_type} record: {data}")

            print("CSV file has been processed successfully.")

 


