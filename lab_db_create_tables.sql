-- Create the Patients table
CREATE TABLE Patients (
    patientId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create the LabTechnicians table
CREATE TABLE LabTechnicians (
    technicianId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create the Doctors table
CREATE TABLE Doctors (
    doctorId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    specialty VARCHAR(255) NOT NULL
);

-- Create the Appointments table to manage appointments between patients and doctors
CREATE TABLE Appointments (
    appointmentId INT AUTO_INCREMENT PRIMARY KEY,
    patientId INT,
    doctorId INT,
    appointmentDate DATE,
    appointmentTime TIME,
    FOREIGN KEY (patientId) REFERENCES Patients(patientId),
    FOREIGN KEY (doctorId) REFERENCES Doctors(doctorId)
);

-- Create the LabWork table to manage lab work scheduled by lab technicians for patients
CREATE TABLE LabWork (
    labWorkId INT AUTO_INCREMENT PRIMARY KEY,
    patientId INT,
    technicianId INT,
    testType VARCHAR(255),
    testDate DATE,
    testTime TIME,
    FOREIGN KEY (patientId) REFERENCES Patients(patientId),
    FOREIGN KEY (technicianId) REFERENCES LabTechnicians(technicianId)
);

-- Create the TestResults table to store test results
CREATE TABLE TestResults (
    resultId INT AUTO_INCREMENT PRIMARY KEY,
    labWorkId INT,
    resultData BLOB,
    resultType VARCHAR(50), -- could be 'PDF', 'JPEG', 'Video', etc.
    FOREIGN KEY (labWorkId) REFERENCES LabWork(labWorkId)
);

-- Create the Payments table to manage payments
CREATE TABLE Payments (
    paymentId INT AUTO_INCREMENT PRIMARY KEY,
    patientId INT,
    amount DECIMAL(10, 2),
    paymentMethod VARCHAR(255),
    paymentDate DATE,
    FOREIGN KEY (patientId) REFERENCES Patients(patientId)
);