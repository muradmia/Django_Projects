from django.shortcuts import render
from . form import LoginForm,StudentForm
# Create your views here.
def app(request):
    return render(request,'app.html')

def form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'form.html',{'form':form})
    else:
        form = LoginForm()
    return render(request,'form.html',{'form':form})

def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request,'model_form.html',{'form' : form})