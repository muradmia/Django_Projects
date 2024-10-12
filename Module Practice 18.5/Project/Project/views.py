from django.shortcuts import render
from posts import models
def home(request):
    return render(request,'home.html')

def show_post(request):
    data = models.post_model.objects.all()
    return render(request,'show_post.html',{'data':data})