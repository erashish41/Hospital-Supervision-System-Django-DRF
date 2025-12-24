from django.urls import path
from management.views import HospitalListView

urlpatterns = [
    path("hospitals", HospitalListView.as_view(),name="hospital_list")
]