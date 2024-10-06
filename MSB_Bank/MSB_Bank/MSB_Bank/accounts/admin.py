from django.contrib import admin
from . models import User_Bank_Account,User_address
from . import models
# Register your models here.
admin.site.register(models.User_Bank_Account)
admin.site.register(models.User_address)