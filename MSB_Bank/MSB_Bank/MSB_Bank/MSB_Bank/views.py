from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
class base(CreateView):
    template_name = 'base.html'

def base(request):
    return render(request,'base.html')