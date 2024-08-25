from django.shortcuts import render
from . import forms
# Create your views here.
def category(request):
    if request.method == 'POST':
        form = forms.category_form(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = forms.category_form()
    return render(request, 'add_category.html',{'form':form})