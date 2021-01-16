from django.urls import include, path
from . import views

urlpatterns = [
    # Aggiunti da me:
    path('diario/', views.diario_list, name='diario'),

]
