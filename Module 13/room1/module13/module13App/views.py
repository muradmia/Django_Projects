from django.shortcuts import render
from . forms import contact,student
# Create your views here.
def app(request):
    return render(request,'app.html')

def form(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        select= request.POST.get('select')
        # form.save()
        return render(request,'form.html',{'name':name, 'email':email,'select' : select})
    else:
        return render(request,'form.html')

def django_form(request):
    form = student(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        print('hello')
    return render(request,'django_form.html',{'form' : form})