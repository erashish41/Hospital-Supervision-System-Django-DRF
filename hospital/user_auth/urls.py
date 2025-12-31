from django.urls import path
from user_auth.views import UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path("signin/", UserRegisterView.as_view(), name='signin'),
    path("login/", UserLoginView.as_view(), name='login'),
    path("logout/", UserLogoutView.as_view(), name='logout'),
]