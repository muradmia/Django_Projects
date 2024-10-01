from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('post',views.post,name = 'post'),
    path('post',views.add_post_create_view.as_view(),name = 'post'),
    path('input',views.input_da.as_view(),name = 'input'),
    # path('edit_post/<int:id>',views.edit_post,name = 'edit_post'),
    path('edit_post/<int:id>',views.update_view.as_view(),name = 'edit_post'),
    # path('delete_post/<int:id>',views.delete_post,name="delete_post"),
    path('delete_post/<int:id>',views.delete_view.as_view(),name="delete_post"),
    
]

