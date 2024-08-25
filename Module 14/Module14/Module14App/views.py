from django.shortcuts import render,redirect
from . forms import student,Student_form,Signup,login
from . import models
# Create your views here.
def app(request):
    return render(request,'app.html')

def django_form(request):
    if request.method == 'POST':
        form = student(request.POST,request.FILES)
    # print(form)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('Module14App/upload' + file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request,'form.html',{'form':form})
    else :
        form = student()
    return render(request,'form.html',{'form':form})

def form(request):
    if request.method == 'POST':
        form = Student_form(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'form.html',{'form' : form})
    else:
        form = Student_form()
    return render(request,'form.html',{'form' : form})

def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'form.html',{'form' : form})
    else:
        form = Signup()
    return render(request,'form.html',{'form' : form})
def student(request):
    st = models.Student.objects.all()
    print(st)
    return render(request,'model.html',{'data' : st})


def delete_student(request,roll):
    st = models.Student.objects.get(pk = roll).delete()
    return redirect('app')

def model_form(request):
    if request.method == 'POST':
        form = login(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = login()
    return render(request,'model_form.html',{'form' : form})