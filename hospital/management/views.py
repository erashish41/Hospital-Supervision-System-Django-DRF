from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from management.models import (
    CustomUser, Hospital, Department, Doctor, Patient,
    Appointment, MedicalRecord, Prescription, Billing
)
# Create your views here.

class HospitalListView(ListView):
    model = Hospital
    context_object_name = "hospitals"
    template_name = "management_templates/hospital_list.html"
    
    