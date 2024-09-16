from django.urls import path
from . import views

urlpatterns = [
    path('commande/<int:commande_id>/edit/', views.edit_commande, name='edit_commande'),
    path('commandes/', views.liste_commandes, name='liste_commandes'),
     path('commandes/add/', views.add_commande, name='add_commande'),
    path('commandes/delete/<int:commande_id>/', views.delete_commande, name='delete_commande'),
    path('commandes/<int:commande_id>/add-formset-row/', views.add_formset_row, name='add_formset_row'),
]