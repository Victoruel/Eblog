from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient


def lipa_na_mpesa(request):
    cl = MpesaClient()

    amount = 1
    phone_number = "0795509620"
    account_reference = "reference"
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)