from django import forms
from . models import signup,login
from . import models

class singup_form(forms.ModelForm):
    class Meta:
        model = signup
        fields = '__all__'

        widgets = {
        'password': forms.PasswordInput(),
        'con_password': forms.PasswordInput(),
    }


class login_form(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'

        widgets = {
            'password': forms.PasswordInput(),
        }

