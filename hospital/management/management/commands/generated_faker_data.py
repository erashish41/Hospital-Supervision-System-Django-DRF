import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from management.models import (
    CustomUser, Hospital, Department, Doctor, Patient,
    Appointment, MedicalRecord, Prescription, Billing
)
from management.constants import GENDER, STATUS, PAID, ROLE_CHOICES

fake = Faker()


def pick_choice(choices):
    """Return only the value part from Django choices"""
    return random.choice([c[0] for c in choices])


class Command(BaseCommand):
    help = "Seed fake data for Hospital Management System"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding fake data...")

        self.create_hospitals(20)
        self.create_departments(6)
        self.create_doctors(100)
        self.create_patients(500)
        self.create_appointments(per_day=10, days=30)
        self.create_medical_records()
        self.create_prescriptions()
        self.create_billings()

        self.stdout.write(self.style.SUCCESS("Fake data created successfully"))


    def create_hospitals(self, count):
        for _ in range(count):
            Hospital.objects.create(
                name=fake.company(),
                email=fake.unique.company_email(),
                address=fake.address(),
                phone=fake.phone_number()[:15],
            )

    def create_departments(self, per_hospital):
        department_names = [
            "Cardiology", "Neurology", "Orthopedics",
            "Pediatrics", "Oncology", "Dermatology"
        ]

        for hospital in Hospital.objects.all():
            for name in department_names[:per_hospital]:
                Department.objects.create(
                    name=name,
                    hospital=hospital
                )

    def create_doctors(self, count):
        departments = list(Department.objects.all())

        for i in range(count):
            user = CustomUser.objects.create_user(
                username=f"doctor{i}",
                email=fake.unique.email(),
                password="test@123",
                role="doctor",
                phone=fake.unique.phone_number()[:15],
                gender=pick_choice(GENDER),
                address=fake.address()
            )

            Doctor.objects.create(
                user=user,
                specialization=fake.job(),
                department=random.choice(departments),
                license_number=f"LIC-{fake.unique.random_int(10000, 99999)}"
            )

    def create_patients(self, count):
        for i in range(count):
            user = CustomUser.objects.create_user(
                username=f"patient{i}",
                email=fake.unique.email(),
                password="test@123",
                role="patient",
                phone=fake.unique.phone_number()[:15],
                gender=pick_choice(GENDER),
                address=fake.address()
            )

            Patient.objects.create(user=user)

    def create_appointments(self, per_day, days):
        patients = list(Patient.objects.all())
        doctors = list(Doctor.objects.all())
        hospitals = list(Hospital.objects.all())

        total = per_day * days

        for _ in range(total):
            Appointment.objects.create(
                patient=random.choice(patients),
                doctor=random.choice(doctors),
                hospital=random.choice(hospitals),
                appointment_date=fake.date_time_between(
                    start_date="-30d",
                    end_date="now",
                    tzinfo=timezone.get_current_timezone()
                ),
                status=pick_choice(STATUS)
            )

    def create_medical_records(self):
        for patient in Patient.objects.all():
            appointment = patient.patient_appointments.first()
            if appointment:
                MedicalRecord.objects.create(
                    patient=patient,
                    doctor=appointment.doctor,
                    appointment=appointment,
                    diagnosis=fake.text(max_nb_chars=200)
                )

    def create_prescriptions(self):
        for appointment in Appointment.objects.all():
            Prescription.objects.create(
                appointment=appointment,
                patient=appointment.patient,
                doctor=appointment.doctor,
                medicine=fake.sentence(nb_words=5)
            )

    def create_billings(self):
        for appointment in Appointment.objects.all():
            Billing.objects.create(
                appointment=appointment,
                amount=random.randint(500, 5000),
                paid=pick_choice(PAID)
            )
