from django.contrib import admin
from . models import musician_model,album_model
from . import models
# Register your models here.
admin.site.register(models.musician_model)
admin.site.register(models.album_model)