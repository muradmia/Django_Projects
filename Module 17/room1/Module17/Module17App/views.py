from django.shortcuts import render
from . forms import singup_form,login_form,registerform
from . import forms 
from django.contrib import messages
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
            messages.success(request,'account Create successful')
            form.save()
    else:
        form = login_form()
    return render(request, 'login.html',{'form':form})

def home(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            messages.success(request,'account Create successful')
            form.save()
            print(form.cleaned_data)
    else:
        form = registerform()
    return render(request, 'signup.html',{'form' : form})