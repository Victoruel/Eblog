from django import forms

from .models import Paper


class PaperForm(forms.ModelForm):

    class Meta:
        model = Paper
        fields = ["title", "file", "author", "topic"]

        widgets = {
            "title": forms.TextInput(),
            "file": forms.FileInput(),
            "author": forms.Select(),
            "topic": forms.Select()
        }
