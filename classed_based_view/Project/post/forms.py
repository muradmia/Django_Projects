from django import forms
from .models import post_model,input_d
from . import models

class post_form(forms.ModelForm):
    class Meta:
        model = post_model
        fields ='__all__'

class input_form(forms.ModelForm):
    class Meta:
        model = input_d
        fields ='__all__'


