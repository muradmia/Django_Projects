

# Create your models here.
from django.db import models

# Create your models here.
class post_model(models.Model):
    name = models.CharField(max_length=15)
    document=models.CharField(max_length=30)
    dc = models.TextField(max_length=500,null = True)
    image = models.ImageField(upload_to = 'posts/media/uploads/',null = True,blank = True)
