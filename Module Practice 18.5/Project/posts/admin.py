from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import post_model
from . import models
# Register your models here.
admin.site.register(models.post_model)