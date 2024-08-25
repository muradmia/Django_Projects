from django.db import models
from django import datetime
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=15)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField(blank=True)
    father_name = models.TextField(blank=True)

    def __str__(self):
        return f"Roll : {self.roll} - Name : {self.name}"