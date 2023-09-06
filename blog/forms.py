from django import forms

from .models import Paper


class PaperForm(forms.ModelForm):

    class Meta:
        model = Paper
        fields = ["title", "file", "author",
                  "topic", "thumbnail", "pages", "price"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "file": forms.FileInput(attrs={
                "class": "form-control"
            }),
            "author": forms.Select(attrs={
                "class": "form-control"
            }),
            "topic": forms.Select(attrs={
                "class": "form-control"
            }),

            "thumbnail": forms.FileInput(attrs={
                "class": "form-control"
            }),
            "pages": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0" 
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0"
            })
        }
