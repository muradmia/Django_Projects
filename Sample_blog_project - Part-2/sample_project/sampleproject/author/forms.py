from django import forms
from .models import Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# class Auth_form(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields ='__all__'


class Registration_form(UserCreationForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'id': 'required'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username']

class Change_userdata(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']