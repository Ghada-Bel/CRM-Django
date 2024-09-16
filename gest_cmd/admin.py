from django.contrib import admin
from .models import Client,Commande,Produit,Ligne_cmd

admin.site.register(Client)
admin.site.register(Commande)
admin.site.register(Produit)
admin.site.register(Ligne_cmd)

