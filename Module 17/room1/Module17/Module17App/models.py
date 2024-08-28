from django.db import models

# Create your models here.
class signup(models.Model):
    username = models.CharField(max_length=15)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    con_password = models.CharField(max_length=15)