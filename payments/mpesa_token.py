import requests
from requests.auth import HTTPBasicAuth
from django_daraja.mpesa.core import MpesaClient
import json

request = ""


# def get_access_token(request):
#     url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
#     headers = {"Authorization": "Basic SWZPREdqdkdYM0FjWkFTcTdSa1RWZ2FTSklNY001RGQ6WUp4ZVcxMTZaV0dGNFIzaA=="
#     }
#     r = requests.request("GET", url, data="", headers=headers)
#     data = json.loads(r.text)
#     access_token = data['access_token']
#     print(f"M-pesa Access Token: {r.text}")


# get_access_token(request)


def get_mpesa_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
    querystring = {"grant_type":"client_credentials"}
    payload = ""
    headers = {"Authorization": "Basic SWZPREdqdkdYM0FjWkFTcTdSa1RWZ2FTSklNY001RGQ6WUp4ZVcxMTZaV0dGNFIzaA=="}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response.text)

    return response


def mpesa(phone_number):
    cl = MpesaClient()

    amount = 1
    # phone_number = "0795509620"
    account_reference = "reference"
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
