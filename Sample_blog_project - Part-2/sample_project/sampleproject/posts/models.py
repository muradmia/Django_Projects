from django.db import models
from categories.models import Category
# from author.models import Author
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    category = models.ManyToManyField(Category) # akta post akta multiple category ar majhe thakte pate
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'Title : {self.title}'