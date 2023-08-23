from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = "auth"
urlpatterns = [
    path("create-account/", views.create_account, name='create-account'),
    path("login/", auth_views.LoginView.as_view(authentication_form=LoginForm,
         template_name="registration/login.html"), name='login'),
]
