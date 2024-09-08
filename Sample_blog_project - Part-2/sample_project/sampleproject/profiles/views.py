from django.shortcuts import render,redirect
# from .forms import profile_form
from . import forms
# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        form  = forms.profile_form()
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.profile_form()
    return render(request,'add_profile.html',{'form': form})