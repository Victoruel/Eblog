import requests
from requests.auth import HTTPBasicAuth
import json

request = ""


def get_access_token(request):
    consumer_key = ""
    consumer_secret = ""
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_create..."
    r = requests.get(api_url, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    data = json.loads(r.text)
    access_token = data['access_token']
    print(f"M-pesa Access Token: {access_token}")


get_access_token(request)
