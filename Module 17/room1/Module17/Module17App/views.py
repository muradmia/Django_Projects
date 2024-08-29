from django.shortcuts import render
from . forms import singup_form,login_form
from . import forms
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = singup_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = singup_form()
    return render(request, 'signup.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = login_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = login_form()
    return render(request, 'login.html',{'form':form})