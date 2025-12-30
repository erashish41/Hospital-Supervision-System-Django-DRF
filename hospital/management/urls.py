from django.urls import path
from management.views import (
    HospitalListView, HospitalDetailView, HospitalDeleteView,
    HospitalUpdateView, HospitalCreateView
)

urlpatterns = [
    path("hospitals/", HospitalListView.as_view(),name="hospital_list"),
    path("hospitals/create/", HospitalCreateView.as_view(),name="hospital_create"),
    path("hospitals/<uuid:pk>/", HospitalDetailView.as_view(),name="hospital_detail"),
    path("hospitals/<uuid:pk>/update/", HospitalUpdateView.as_view(),name="hospital_update"),
    path("hospitals/<uuid:pk>/delete/", HospitalDeleteView.as_view(),name="hospital_delete")
]