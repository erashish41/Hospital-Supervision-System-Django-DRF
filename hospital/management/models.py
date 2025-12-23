from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.models import BaseMixin
from management.constants import GENDER, STATUS, PAID, ROLE_CHOICES

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER)
    address = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=5, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    REQUIRED_FIELDS = []

    

class Hospital(BaseMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length= 200)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.name} - {self.address}"
    
    
class Department(BaseMixin):
    name = models.CharField(max_length=100)
    hospital = models.ForeignKey("Hospital", on_delete=models.CASCADE, related_name="departments")
    
    def __str__(self):
        return f"{self.name}"

class Doctor(BaseMixin):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, related_name="doctor_profile")
    specialization = models.CharField(max_length=100)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.specialization}"
    
    
class Patient(BaseMixin):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, related_name="patient_profile")
    
    def __str__(self):
        return f"{self.user.get_full_name()}"


class Appointment(BaseMixin):
    patient = models.ForeignKey("Patient",on_delete=models.CASCADE, related_name="patient_appointments")
    appointment_date = models.DateTimeField()
    hospital = models.ForeignKey("Hospital", on_delete=models.CASCADE)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, related_name="doctor_appointments")
    status = models.CharField(choices=STATUS, max_length=20,default="pending")
    
    def __str__(self):
        return f"{self.patient.user.username} - {self.appointment_date}"
    
class MedicalRecord(BaseMixin):
    patient = models.ForeignKey("Patient",on_delete=models.CASCADE, related_name="patient_medical")
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, related_name="doctor_medical")
    diagnosis = models.TextField()
    appointment = models.ForeignKey("Appointment", on_delete=models.CASCADE, related_name="medical_appointment")

    
    def __str__(self):
        return f"{self.patient.user.get_full_name()} - {self.diagnosis}"
    

class Prescription(BaseMixin):
    appointment = models.ForeignKey("Appointment", on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient",on_delete=models.CASCADE)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    medicine = models.TextField()
    
    def __str__(self):
        return f"{self.appointment.patient.user.get_full_name()} - {self.medicine}"
    

class Billing(BaseMixin):
    appointment = models.OneToOneField("Appointment", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.CharField(choices=PAID, max_length=3, default="no")
    
    def __str__(self):
        return f"{self.amount} - {self.paid}"