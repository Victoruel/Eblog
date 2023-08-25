from django import forms
from .models import HelpRequest


class HelpRequestForm(forms.ModelForm):

    class Meta:
        model = HelpRequest
        fields = ("paper_type", "study_level", "pages", "days", "description")

        widgets = {
            "paper_type": forms.Select(attrs={
                "class": "rounded"
            }),
            "study_level": forms.Select(attrs={
                "class": "rounded"
            }),
            "pages": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "1"
            }),
            "days": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "1",
                "max": "5"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Type your instructions here.Please provide as many details as possible."
            })
        }
