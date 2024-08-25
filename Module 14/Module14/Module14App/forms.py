from django import forms
from django.core import validators
from . models import Model_form
class student(forms.Form):
    name = forms.CharField(max_length=15,label="Name :",initial="rahim",help_text="Enter your name.")
    file = forms.FileField()
    email = forms.CharField(max_length=15)
    Age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs = {'type' : 'date'}))
    appointment_date = forms.DateTimeField()
    CHOICE =[('S','Small'),('M','Medium'),('L','large')]
    size = forms.ChoiceField(choices=CHOICE)

class Student(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget = forms.EmailInput)

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at list 10 chracter")
    #     return valname

    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("your email is not valid")
    #     return valemail

    # def clean(self):
    #     clean_data = super().clean()
    #     valname = self.cleaned_data['name']

    #     if len(valname) < 10:
    #         raise forms.ValidationError('erorr')

class Student_form(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,"enter a name at list 10 chracter")])
    email = forms.CharField(widget=forms.EmailInput)
    age = forms.CharField()


class Signup(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        valconpass = self.cleaned_data['confirm_password']

        if valpass != valconpass:
            raise forms.ValidationError("Password doesn't Match")

class login(forms.ModelForm):
    class Meta:
        model = Model_form
        fields = '__all__'
        exclude = ['roll']

        labels = {
            'name' : 'Name' 
        }

        widgets = {
            'name' : forms.TextInput(attrs = {'class': 'btn-primary'}),
        }
        help_texts = {
            'name' : 'Enter your name'
        }

        error_messages = {
            'name' : {'required' : 'name is need'}
        }
