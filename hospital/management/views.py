from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from management.models import (
    CustomUser, Hospital, Department, Doctor, Patient,
    Appointment, MedicalRecord, Prescription, Billing
)

# Create your views here.

class HospitalListView(ListView):
    model = Hospital
    context_object_name = "hospitals"
    template_name = "management_templates/hospital_list.html"
    

class HospitalUpdateView(DetailView):
    model = Hospital
    context_object_name = "hospital"
    template_name = "management_templates/hospital_detail.html"

class HospitalDeleteView(DeleteView):
    model = Hospital
    success_url = reverse_lazy("hospital_list")