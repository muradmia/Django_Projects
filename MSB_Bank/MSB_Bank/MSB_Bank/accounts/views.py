from django.shortcuts import render
from django.views.generic import FormView
from .form import User_Registaion_form
from django.contrib.auth import login
# Create your views here.
def account_create(request):
    return render(request,'create_account.html')

class UserRegestation(FormView):
    template_name = 'create_account.html'
    form_class = User_Registaion_form
    # success_url = 'base'
    def form_valid(self,form):
        ser = form.save()
        login(ser)
        return super().form_valid(form)