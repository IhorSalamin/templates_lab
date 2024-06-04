from flask import Flask, render_template, request, redirect, url_for, session
from frontend.models.patient import Patient
from backend.business_logic.services import PatientService

from main import app
#app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
#    # Тестові дані, в майбутньому замінимо запитами до бази даних
#    test_patients = [Patient("test@gmail.com", "password")]

#    print(test_patients)
#    return render_template('index.html', patients=test_patients)
    print("session before")
    if 'patient' in session:
            patient = session['patient']
            # Тут створюємо список пацієнтів для демонстрації
            test_patients = [Patient(**patient)]  # Розпаковуємо дані з сесії до об'єкта Patient
            print(test_patients)
            
            pdata = PatientService()
            test_data = pdata.get_patient_data(test_patients[0])


            return render_template('index.html', patient=test_data)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print("login start")
        if email and password:
            patient = Patient(email=email, password=password)
            session['patient'] = patient.__dict__
            print(patient)
            return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/add', methods=['POST'])
def add_patient():
    # Логіка додавання пацієнта
    pass

@app.route('/edit/<int:id>', methods=['POST'])
def edit_patient(id):
    # Логіка редагування пацієнта
    pass

@app.route('/delete/<int:id>', methods=['POST'])
def delete_patient(id):
    # Логіка видалення пацієнта
    pass
