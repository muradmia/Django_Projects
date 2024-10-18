from django import forms
from .models import User_Bank_Account,User_address,demo
from .constants import ACCOUNT_TYPE,GENDER
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class User_Registaion_form(UserCreationForm):
    # birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=30)
    # city = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields=['username', 'password1','password2', 'first_name','last_name', 'email','gender','postal_code','country','city','address']
        # fields = ['username','first_name','last_name','email']

    def save(self,commit= True):
        our_user = super().save()
        if commit == True:
            our_user.save()#user ar model ar data save korlam
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
            city = self.cleaned_data.get('city')
            address = self.cleaned_data.get('address')

            User_address.objects.create(
                user = our_user,
                postal_code = postal_code,
                country = country,
                address = address,
            )

            User_Bank_Account.objects.create(
                user = our_user,
                # birth_date = birth_date,
                gender = gender,
                account_no = 10000+our_user.id
            )
            return our_user

class demo_model(forms.ModelForm):
    class Meta:
        model = demo
        fields ='__all__'
