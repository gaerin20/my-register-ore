from django.urls import path
from . import views

urlpatterns = [
 path('blog', views.post_list, name = 'post_list'),
]
