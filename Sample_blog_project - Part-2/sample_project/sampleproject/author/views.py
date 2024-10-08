from django.shortcuts import render,redirect
from . forms import Registration_form,Change_userdata
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
            messages.success(request,"Account Created Success")
            print(form.cleaned_data)
            return redirect('login')
    else:
        form = forms.Registration_form()
    return render(request,'register.html',{'form':form,'type' : 'Register'})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request,data = request.POST)
        if form.is_valid():
            usernam = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = usernam,password = userpass)
            if user is not None:
                messages.success(request,"Login Success")
                login(request,user)
                return redirect('profile')
            else:
                messages.success(request,"Login Faild")    
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'form' : form,'type' : 'Login'})
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = Change_userdata(request.POST,instance = request.user)
        if form.is_valid():
            messages.success(request,"Account Update Success")
            form.save()
            return redirect('profile')
    else:
        form = Change_userdata(instance = request.user)
    return render(request,'update_profile.html',{'form' : form})

@login_required
def Change_userData(request):
    return render(request,'profile.html')
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            messages.success(request,"Password Update  Success")
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request,'pass_change.html',{'form' : form})