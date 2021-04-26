from django.urls import include, path
from . import views

urlpatterns = [
    # Aggiunti da me:
    path('addOre/', views.addOre, name='addOre'),
    path('reportOre/', views.reportOre, name='reportOre'),
    path('reportOreND/', views.reportOreND, name='reportOreND'),
    path('export_csv/', views.export_csv, name='export_csv'),
    path('listing_ore/', views.listing_ore, name='listing_ore'),
    path('update_ore/<int:ore_id>/', views.update_ore, name='update_ore'),
    path('prodiario/', views.addDiario, name='diario'),
    path('prodiarioList/', views.diario_list, name='diario-list'),
    path('listing_diario/', views.listing_diario, name='listing_diario'),
    path('view_diario/<int:diario0_id>/', views.view_diario, name='view_diario'),
    path('update_diario/<int:diario0_id>/', views.update_diario, name='update_diario'),
]
