from management.forms import CustomUserForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = "user_auth_template/signin.html"
    success_url = reverse_lazy('login')
    
    
    
class UserLoginView(LoginView):
    template_name = "user_auth_template/login.html"
    success_url = reverse_lazy("hospital_list")
    
    
    
class UserLogoutView(LogoutView):
    success_url = reverse_lazy("signin")