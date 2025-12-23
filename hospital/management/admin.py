from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from management.models import (
    CustomUser, Hospital, Department, Doctor, Patient, 
    Appointment, MedicalRecord, Prescription, Billing
)


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'username', 'first_name', 'last_name', 'is_active', 
        'is_superuser', 'is_staff', 'gender'
    )
    list_filter = (
        'is_active', 'is_staff', 'is_superuser'
    )
    
@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'address', 'phone',
    )
    list_filter = ('name', 'address')
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'hospital_name')
    list_filter = ('hospital',)
    
    def hospital_name(self, obj):
        return obj.hospital.name
    hospital_name.short_description = 'Hospital'
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'get_username',
        'get_email',
        'get_phone',
        'specialization',
        'department',
        'license_number',
    )

    list_filter = (
        'specialization',
        'department',
    )

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_phone(self, obj):
        return obj.user.phone
    get_phone.short_description = 'Phone'

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('get_username',)
    list_filter = ('user',)
    
    def get_username(self,obj):
        return obj.user.username
    get_username.short_description = "Username"
    

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = (
        'appointment', 'amount', 'paid'
    )
    list_filter = ('appointment', 'paid')

admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Prescription)