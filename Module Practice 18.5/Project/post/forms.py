from django import forms
from .models import post_model
from . import models

class post_form(forms.ModelForm):
    class Meta:
        model = post_model
        fields ='__all__'
