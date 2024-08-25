from django.shortcuts import render,redirect
from posts.models import Post
def base(request):
    return render(request,'base.html')

def home(request):
    data = Post.objects.all()
    print(data)
    return render(request,'home.html',{'data':data})