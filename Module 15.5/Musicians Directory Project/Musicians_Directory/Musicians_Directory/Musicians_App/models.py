from django.db import models

# Create your models here.
class musician_model(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField(max_length=15)
    instrument_type = models.CharField(max_length=30)

    def __str__(self):
        return f'Name : {self.first_name}'

class album_model(models.Model):
    album_name = models.CharField(max_length=30)
    album_relese_date = models.DateTimeField(auto_now_add=True)
    relations = models.ForeignKey(musician_model,on_delete=models.CASCADE)

    def __str__(self):
        return f'Name : {self.album_name}'