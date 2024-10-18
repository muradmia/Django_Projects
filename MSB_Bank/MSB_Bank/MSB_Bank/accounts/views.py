from django.shortcuts import render
from django.views.generic import FormView,CreateView
from .form import User_Registaion_form,demo_model
from django.contrib.auth import login
from .models import demo
from . import models
from . import form
from django.urls import reverse_lazy
# Create your views here.
def account_create(request):
    return render(request,'create_account.html')

class UserRegestation(FormView):
    template_name = 'create_account.html'
    form_class = User_Registaion_form
    success_url = reverse_lazy('base')
    def form_valid(self,form):
        # form.instance.author = self.request.use
        print(form.cleaned_data)
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)

class demoq(CreateView):
    model = models.demo
    template_name = 'demo.html'
    form_class = form.demo_model
    success_url = reverse_lazy('base')
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    