import os
from data_access.database import DatabaseManager
from data_access.repository import Repository
from data_access.models import Patient

from business_logic.services import CSVReader 


def main():
    #db_manager = DatabaseManager()  # Створюємо екземпляр менеджера бази даних
    #session = db_manager.create_session()  # Створюємо сесію через менеджер

    #try:
    #    db_manager.check_connection(session)  # Перевірка з'єднання з базою даних
    #    print("Database connection is successful.")
    #except Exception as e:
    #    print(f"Failed to connect to the database: {str(e)}")
    #finally:
    #    db_manager.close_session(session)  # Завжди закриваємо сесію
        

    # Створюємо екземпляр репозиторію
    repo = Repository()

    # Створюємо екземпляр business_logic CVSRead


    csvRead = CSVReader()
    
    # Імпортуємо дані пацієнтів з CSV файлу
    dir_path = os.path.dirname(os.path.abspath(__file__))  # Директорія, де знаходиться main.py
    csv_file_path = os.path.join(dir_path, 'data.csv')  # Повний шлях до файлу data.csv
    #repo.import_data_from_csv(csv_file_path)

    csvRead.read(csv_file_path)
    csvRead.write_to_database()
    
    # Отримуємо всіх пацієнтів з бази даних
    all_patients = repo.get_all_patients()
    
    # Виводимо дані пацієнтів
    if all_patients:
        for patient in all_patients:
            print(f"Patient ID: {patient.patientId}, Name: {patient.name}, Email: {patient.email}")
    else:
        print("No patients found in the database.")

if __name__ == "__main__":
    main()
