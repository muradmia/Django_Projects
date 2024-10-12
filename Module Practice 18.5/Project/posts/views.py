from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . import models
from .models import post_model
# Create your views here.
from django.shortcuts import render
from .forms import post_form
from . import forms
from django.views.generic import DetailView
# Create your views here.
def post(request):
    if request.method == 'POST':
        form = post_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = post_form()
    return render(request, 'post.html',{'form':form})

def edit_post(request,id):
    post = models.post_model.objects.get(pk=id)
    form = forms.post_form(instance=post)
    if request.method == 'POST':
        form = post_form(request.POST, request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'post.html',{'form':form})

def delete_post(request,id):
    post = models.post_model.objects.get(pk=id)
    post.delete()
    return redirect('home')


class details_view(DetailView):
    pk_url_kwargs = 'pk'
    model = post_model
    template_name = 'post_details.html'