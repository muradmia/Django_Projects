from django.shortcuts import render
# from . forms import Auth_form
from . import forms
# Create your views here.
def add_author(request):
    if request.method == 'POST':
        form = forms.Auth_form(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = forms.Auth_form()
    return render(request,'add_author.html',{'form':form})

    # form = forms.Auth_form()
    # return render(request,'add_author.html',{'form':form})
