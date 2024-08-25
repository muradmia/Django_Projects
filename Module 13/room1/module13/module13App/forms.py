from django import forms

class contact(forms.Form):
    name = forms.CharField(max_length=15,label = 'Name')
    email = forms.CharField(max_length=20)

class student(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()