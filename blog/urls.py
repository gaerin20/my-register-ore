from django.urls import path, include
from . import views

urlpatterns = [
 path('blog', views.post_list, name = 'post_list'),
 path('', views.listing, name = 'listing'),
 path('view_blog/<int:blog_id>/', views.view_blog, name = 'view_blog'),
 path("see_request/", views.see_request),
 path("spazio_privato/", views.spazio_privato),
 path("accounts", include("django.contrib.auth.urls")),
 path("staff_place/", views.staff_place),
 path("add_messages", views.add_messages),
]
