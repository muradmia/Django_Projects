from django.shortcuts import render,redirect
from . import forms
from . forms import musician_form,album_form
from . import models
# Create your views here.
def musicians(request):
    if request.method == 'POST':
        form = musician_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = musician_form()
    return render(request, 'Musicians.html' , {'form': form})
def album(request):
    if request.method == 'POST':
        form  = album_form(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = album_form()
    return render(request,'album.html',{'form': form})

def edit(request,id):
    post = models.album_model.objects.get(pk=id)
    print(post)
    form  = album_form(instance=post)
    if request.method == 'POST':
        form  = album_form(request.POST,instance=post)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    return render(request,'album.html',{'form': form})

def delete(request,id):
    post = models.album_model.objects.get(pk=id)
    post.delete()
    return redirect('home')
