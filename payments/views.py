from django.shortcuts import render, get_object_or_404
from django_daraja.mpesa.core import MpesaClient

from blog.models import Paper
from .forms import Mpesa_form
from .mpesa_token import mpesa


def lipa_na_mpesa(request):
    cl = MpesaClient()

    amount = 1
    phone_number = "0795509620"
    account_reference = "reference"
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

def payment_page(request, paper_id):
    
    paper = get_object_or_404(Paper, id = paper_id)

    form = Mpesa_form(request.POST or None)

    if form.is_valid():
        phone_no = form.cleaned_data["phone_no"]
        mpesa(phone_no)

        form = Mpesa_form()
        print(phone_no)

    print(paper)
    
    context ={
        "paper": paper,
        "form": form
    }

    return render(request, "payments/payments.html", context)