from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.add_post,name = 'add_post'),
    path('edit/<int:id>',views.edit,name = 'edit'),
    path('delete/<int:id>',views.delete,name = 'delete')
]