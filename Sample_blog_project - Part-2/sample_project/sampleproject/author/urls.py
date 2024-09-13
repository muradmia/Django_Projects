from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('register/',views.Register,name = 'register'),
    path('login/',views.login_user,name = 'login'),
    path('profile',views.Change_userData,name = 'profile'),
    path('profile/edit//passchange/',views.pass_change,name = 'passchange'),
    path('profile/edit',views.edit_profile,name = 'edit_profile'),

]