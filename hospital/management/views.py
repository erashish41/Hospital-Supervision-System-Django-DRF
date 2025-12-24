from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )
from management.models import (
    CustomUser, Hospital, Department, Doctor, Patient,
    Appointment, MedicalRecord, Prescription, Billing
)
from management.forms import HospitalForm

# Create your views here.

class HospitalListView(ListView):
    model = Hospital
    context_object_name = "hospitals"
    template_name = "management_templates/hospital_list.html"
    

class HospitalDetailView(DetailView):
    model = Hospital
    context_object_name = "hospital"
    template_name = "management_templates/hospital_detail.html"


class HospitalCreateView(CreateView):
    model = Hospital
    form_class = HospitalForm
    success_url = reverse_lazy("hospital_list")

class HospitalDeleteView(DeleteView):
    model = Hospital
    success_url = reverse_lazy("hospital_list")