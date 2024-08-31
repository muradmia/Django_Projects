from django.shortcuts import render,redirect
from . forms import singup_form,login_form,registerform
from . import forms 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = singup_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = singup_form()
    return render(request, 'signup.html',{'form':form})

# def login(request):
#     if request.method == 'POST':
#         form = login_form(request.POST, request.FILES)
#         if form.is_valid():
#             messages.success(request,'account Create successful')
#             form.save()
#     else:
#         form = login_form()
#     return render(request, 'login.html',{'form':form})

def home(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            messages.success(request,'account Create successful')
            form.save()
            print(form.cleaned_data)
    else:
        form = registerform()
    return render(request, 'home.html',{'form' : form})

def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request,data = request.POST)
        if form.is_valid():
            usernam = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username = usernam, password = upass) #check user in database or not

            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form' : form})


