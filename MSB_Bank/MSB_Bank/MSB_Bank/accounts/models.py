from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER
# Create your models here.
#django has a buildin usermake

class User_Bank_Account(models.Model):
    user = models.OneToOneField(User,related_name = 'account',on_delete = models.CASCADE)
    account_type = models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    # birth_date = models.DateField(null = True)
    gender = models.CharField(max_length=20,choices=GENDER)
    initial_deposit_date = models.DateField(auto_now_add = True)
    balance = models.DecimalField(default = 0,max_digits=12,decimal_places=2) 

    def __str__(self):
        return f'Account No: {self.account_no}'


class User_address(models.Model):
    user = models.OneToOneField(User,related_name = 'address',on_delete = models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=30)

    def __str__(self):
        return f'Email: {self.user.email}'

class demo(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()