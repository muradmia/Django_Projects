from django import forms
from . models import Student
class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput)
    password = forms.CharField(widget= forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valname = cleaned_data['username']
        valpassword = cleaned_data['password']
        if valname != 'muradmia901':
            raise forms.ValidationError("User name not fount")

        if valpassword != '1234':
            raise forms.ValidationError("Enter correct password")

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
