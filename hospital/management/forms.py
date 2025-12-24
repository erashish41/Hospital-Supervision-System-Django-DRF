from django import forms
from management.models import (
    CustomUser, Hospital, Department, Doctor, Patient,
    Appointment, MedicalRecord, Prescription, Billing
)

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ["name", "email", "address", "phone"]