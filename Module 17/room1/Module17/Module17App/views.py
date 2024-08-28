from django.shortcuts import render
from . forms import singup_form
from . import forms
# Create your views here.
def signup(request):
    form = singup_form()
    return render(request, 'signup.html',{'form':form})