from django.shortcuts import render
from django.views.generic import FormView,CreateView
from django.contrib.auth.views import LoginView
from . form import User_Registaion_form
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import demo
from . import models
from . import form
from django.urls import reverse_lazy
# Create your views here.
def account_create(request):
    return render(request,'create_account.html')

class User_Registaion_form(FormView):
    template_name = 'create_account.html'
    form_class = User_Registaion_form
    # model = models.User
    def get_success_url(self):
        return reverse_lazy('login')
    # success_url = reverse_lazy('base')
    def form_valid(self,form):
        # form.instance.author = self.request.use
        print(form.cleaned_data)
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)

class login1(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')

        def form_valid(self, form):
            messages=(self.request,'logged in successfull')
            return super().form_valid(form)

        def form_invalid(self, form):
            messages=(self.request,'logged in Fail')
            return super().form_invalid(form)
        

    