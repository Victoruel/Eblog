from django import forms

class Mpesa_form(forms.Form):
    phone_no = forms.CharField(max_length=12)