import csv
import os

def save_data_to_csv(data, filename='data.csv'):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def collect_data(entity):
    fields = {
        'Patients': ['name', 'phone', 'email', 'password'],
        'Doctors': ['name', 'specialty'],
        'LabTechnicians': ['name'],
        'Appointments': ['patientId', 'doctorId', 'appointmentDate', 'appointmentTime'],
        'LabWork': ['patientId', 'technicianId', 'testType', 'testDate', 'testTime'],
        'TestResults': ['labWorkId', 'resultData', 'resultType'],
        'Payments': ['patientId', 'amount', 'paymentMethod', 'paymentDate']
    }

    data = {'entity': entity}
    for field in fields[entity]:
        data[field] = input(f"Enter {field}: ")

    return data

def main():
    entities = ['Patients', 'Doctors', 'LabTechnicians', 'Appointments', 'LabWork', 'TestResults', 'Payments']
    while True:
        print("\nSelect the entity to input data or Exit:")
        for index, entity in enumerate(entities, 1):
            print(f"{index}. {entity}")
        print(f"{len(entities) + 1}. Exit")

        choice = int(input("Enter your choice: "))
        if choice == len(entities) + 1:
            break

        entity = entities[choice - 1]
        data = collect_data(entity)
        save_data_to_csv(data)
        print("Data has been saved successfully.")

if __name__ == "__main__":
    main()
