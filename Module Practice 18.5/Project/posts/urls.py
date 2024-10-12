from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('post',views.post,name = 'post'),
    path('edit_post/<int:id>',views.edit_post,name = 'edit_post'),
    path('delete_post/<int:id>',views.delete_post,name="delete_post"),
    path('details/<int:pk>',views.details_view.as_view(),name="details_view"),
]

