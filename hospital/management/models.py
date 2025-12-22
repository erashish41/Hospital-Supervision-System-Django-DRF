from django.db import models
from django.contrib.auth.models import User
from utils.models import BaseMixin

# Create your models here.

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

STATUS = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
)

PAID = (
    ('yes', 'Yes'),
    ('no', 'No'),
)

class Hospital(BaseMixin):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length= 200)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.name} - {self.address}"
    
    
class Department(BaseMixin):
    name = models.CharField(max_length=100)
    hospital = models.ForeignKey("Hospital", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"

class Doctor(BaseMixin):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    hospital = models.ManyToManyField("Hospital", related_name="hospital_doctor")
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.specialization}"
    
    
class Patient(BaseMixin):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    gender = models.CharField(choices=GENDER, max_length=1)
    hospital = models.ManyToManyField("Hospital", related_name="hospital_patient")
    doctor = models.ManyToManyField("Doctor", related_name="doctor_patient")
    
    def __str__(self):
        return f"{self.name} - {self.gender}"


class Appointment(BaseMixin):
    patient = models.ForeignKey("Patient",on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    hospital = models.ForeignKey("Hospital", on_delete=models.CASCADE)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=20,)
    
    def __str__(self):
        return f"{self.patient.name} - {self.date}"
    
class MedicalRecord(BaseMixin):
    patient = models.ForeignKey("Patient",on_delete=models.CASCADE)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, related_name="medical_records")
    diagnosis = models.TextField()
    
    def __str__(self):
        return f"{self.patient.name} - {self.diagnosis}"
    

class Prescription(BaseMixin):
    appointment = models.ForeignKey("Appointment", on_delete=models.CharField)
    patient = models.ForeignKey("Patient",on_delete=models.CASCADE)
    doctor = models.ManyToManyField("Doctor", related_name="prescriptions")
    medicine = models.TextField()
    
    def __str__(self):
        return f"{self.appointment.patient.name} - {self.medicine}"
    

class Billing(BaseMixin):
    appointment = models.ForeignKey("Appointment", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.CharField(choices=PAID, max_length=3)
    
    def __str__(self):
        return f"{self.amount} - {self.paid}"