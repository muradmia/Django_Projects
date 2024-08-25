from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_post(request):
    if request.method == 'POST':
        form = forms.post_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.post_form()
    return render(request, 'add_post.html',{'form':form})

def edit(request,id):
    post = models.Post.objects.get(pk=id)
    form = forms.post_form(instance=post)
    # print(post.title)
    if request.method == 'POST':
        form = forms.post_form(request.POST,instance=post)
        if form.is_valid():
            form.save()

    return render(request, 'add_post.html',{'form':form})

def delete(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')