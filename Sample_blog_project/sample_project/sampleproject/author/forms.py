from django import forms
from .models import Author

class Auth_form(forms.ModelForm):
    class Meta:
        model = Author
        fields ='__all__'
