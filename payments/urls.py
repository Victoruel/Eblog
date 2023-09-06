from django.urls import path

from . import views

app_name = "payments"
urlpatterns = [
    path("<int:paper_id>/", views.payment_page, name="payments-page"),
    path("lipa_na_mpesa/", views.lipa_na_mpesa, name="lipa-na-mpesa"),
]
