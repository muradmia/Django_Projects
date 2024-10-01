from django.contrib import admin
from .models import post_model,input_d
from . import models
# Register your models here.
admin.site.register(models.post_model)
admin.site.register(models.input_d)