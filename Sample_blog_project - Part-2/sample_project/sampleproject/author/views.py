from django.shortcuts import render,redirect
from . forms import Registration_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from . import forms
# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         form = forms.Auth_form(request.POST)
#         if form.is_valid():
#             form.save()
#             print(form.cleaned_data)
#     else:
#         form = forms.Auth_form()
#     return render(request,'add_author.html',{'form':form})

    # form = forms.Auth_form()
    # return render(request,'add_author.html',{'form':form})


def Register(request):
    if request.method == 'POST':
        form = forms.Registration_form(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('register')
    else:
        form = forms.Registration_form()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request,data = request.POST)
        if form.is_valid():
            usernam = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = usernam,password = userpass)
            if user is not none:
                login(request,user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'form' : form})