from django.db import models
# from author.models import Author
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=15)
    about = models.CharField(max_length=100)
    author = models.OneToOneField(User ,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f'Name : {self.name}'