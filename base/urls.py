from django.urls import path
from . import views

app_name = "base"
urlpatterns = [
    path("", views.index, name="index"),
    path("help/", views.price_calculator, name="calculator")
]