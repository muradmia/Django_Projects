from django import forms
from . models import signup
from . import models

class singup_form(forms.ModelForm):
    class Meta:
        model = signup
        fields = '__all__'