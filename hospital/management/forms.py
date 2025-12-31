from django import forms
from management.models import (
    CustomUser, Hospital, Department, Doctor, Patient,
    Appointment, MedicalRecord, Prescription, Billing
)


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email"]

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ["name", "email", "address", "phone"]