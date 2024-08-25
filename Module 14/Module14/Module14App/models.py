from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    roll = models.IntegerField(max_length=100,primary_key=True,default=True)

    def __str__(self):
        return f"Name : {self.name}"


class Model_form(models.Model):
    name = models.CharField(max_length=15)
    address = models.CharField(max_length=30)
    father  = models.CharField(max_length=15)
    roll = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"Name : {self.name}" 