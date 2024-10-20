from django.shortcuts import render
from django.views.generic import TemplateView
from accounts import models
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'