from django.urls import include, path
from . import views

urlpatterns = [
    # Aggiunti da me:
    path('addOre/', views.addOre, name='addOre'),
    path('reportOre/', views.reportOre, name='reportOre'),
    path('reportOreND/', views.reportOreND, name='reportOreND'),
    path('export_csv/', views.export_csv, name='export_csv'),
]
