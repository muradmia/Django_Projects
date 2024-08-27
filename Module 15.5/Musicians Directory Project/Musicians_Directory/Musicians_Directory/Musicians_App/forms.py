from django import forms
from . import models
from . models import musician_model,album_model
class musician_form(forms.ModelForm):
    class Meta:
        model = musician_model
        fields = '__all__'

        def __str__(self):
            return f'name : {self.first_name}'

class album_form(forms.ModelForm):
    class Meta:
        model = album_model
        fields = '__all__' 

        def __str__(self):
            return f'name : {self.album_name}'

