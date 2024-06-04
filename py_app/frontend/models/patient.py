
class Patient:
    def __init__(self, email, password, patientId=0, name="John Doe", phone="0991234567"):
        self.patientId = patientId
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone


    def __repr__(self):
        return f"Patient(patientId={self.patientId}, name='{self.name}', email='{self.email}',password='{self.password}', phone='{self.phone}')"


    # Припустимо, тут буде логіка взаємодії з базою даних


