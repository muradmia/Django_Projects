from django.contrib import admin
from . import models
from . models import signup,login
# Register your models here.
admin.site.register(models.signup)
admin.site.register(models.login)