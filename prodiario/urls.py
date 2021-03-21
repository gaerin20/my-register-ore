from django.urls import include, path
from . import views

urlpatterns = [
    # Aggiunti da me:
    path('prodiario/', views.addDiario, name='diario'),
    path('prodiarioList/', views.diario_list, name='diario-list'),
]
