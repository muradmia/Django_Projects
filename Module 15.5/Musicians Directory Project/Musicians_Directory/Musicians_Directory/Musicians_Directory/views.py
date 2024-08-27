from django.shortcuts import render
from Musicians_App.models import album_model

def home(request):
    data = album_model.objects.all()
    print(data)
    return render(request, 'home.html',{'data':data})

def base(request):
    return render(request, 'base.html')