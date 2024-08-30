from django import forms
from . models import signup,login
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registerform(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']



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

