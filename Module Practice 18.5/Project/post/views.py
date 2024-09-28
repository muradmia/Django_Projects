from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import post_form
from . import forms
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