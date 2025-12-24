from django.urls import path
from management.views import HospitalListView, HospitalUpdateView, HospitalDeleteView

urlpatterns = [
    path("hospitals/", HospitalListView.as_view(),name="hospital_list"),
    path("hospitals/<uuid:pk>", HospitalUpdateView.as_view(),name="hospital_detail"),
    path("hospitals/<uuid:pk>/delete", HospitalDeleteView.as_view(),name="hospital_delete")
]