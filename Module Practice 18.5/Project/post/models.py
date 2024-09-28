from django.db import models

# Create your models here.
class post_model(models.Model):
    name = models.CharField(max_length=15)
    document=models.CharField(max_length=30)