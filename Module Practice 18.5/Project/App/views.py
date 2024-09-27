from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import sign
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = sign(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Sign Up Successfully')
            print(form.cleaned_data)
            return redirect('login')
    else:
        form = sign()
    return render(request,'form.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request,data = request.POST)
        if form.is_valid():
            usernam = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username = usernam, password = upass)
            if user is not None:
                messages.success(request,'Logged In Successfully')
                login(request,user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request,'login_form.html',{'form':form})

def logout_user(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('login')