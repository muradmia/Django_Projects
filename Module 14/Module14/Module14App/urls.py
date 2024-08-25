from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',views.app,name = 'app'),
    path('django_form/',views.signup,name = 'django_form'),
    path('model,',views.student,name = 'model'),
    path('delete/<int:roll>',views.delete_student,name = 'delete'),
    path('model/',views.model_form,name = 'model_form')
]