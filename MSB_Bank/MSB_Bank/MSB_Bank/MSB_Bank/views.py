from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.models import models
# class base(CreateView):
#     template_name = 'base.html'

def base(request):
    # data = models.User_Bank_Account.objects.all()
    return render(request,'base.html')