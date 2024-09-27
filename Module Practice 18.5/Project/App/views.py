from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import sign
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = sign(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = sign()
    return render(request,'form.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request,data = request.POST)
        if form.is_valid():
            usernam = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username = usernam, password = upass)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'login_form.html',{'form':form})