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
from django.contrib import messages

# Create your views here.

class HospitalListView(ListView):
    model = Hospital
    context_object_name = "hospitals"
    template_name = "hospital_template/hospital_list.html"
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["HospitalForm"] = HospitalForm()
        return context
    
    
class HospitalDetailView(DetailView):
    model = Hospital
    context_object_name = "hospital"
    template_name = "hospital_template/hospital_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = HospitalForm(instance=self.object)
        return context
    
    
class HospitalCreateView(CreateView):
    model = Hospital
    form_class = HospitalForm
    success_url = reverse_lazy("hospital_list")
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        messages.success(self.request, "Hospital created successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Failed to create hospital. Please check the form.")
        return super().form_invalid(form)

    
    
class HospitalUpdateView(UpdateView):
    model = Hospital
    form_class = HospitalForm
    success_url = reverse_lazy("hospital_list")
    
    def form_valid(self, form):
        hospital = form.save(commit=False)
        hospital.updated_by = self.request.user
        hospital.save()
        messages.success(self.request, "Hospital updated successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Failed to update hospital. Please check the form")
        return super().form_invalid(form)
    
        
class HospitalDeleteView(DeleteView):
    model = Hospital
    success_url = reverse_lazy("hospital_list")
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Hospital deleted successfully")
        return super().delete(request, *args, **kwargs)
    
    
