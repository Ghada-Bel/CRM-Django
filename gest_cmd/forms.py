from django import forms
from django.forms import inlineformset_factory
from .models import Commande, Ligne_cmd, Produit, Client  # Import Client model

# Define a form for Ligne_cmd model (optional if you need custom form behavior)
class LigneCmdForm(forms.ModelForm):
    class Meta:
        model = Ligne_cmd
        fields = ['code_prod', 'Qte', 'prix']

# Create an inline formset factory for Ligne_cmd related to Commande
LigneCmdFormSet = inlineformset_factory(Commande, Ligne_cmd, form=LigneCmdForm, extra=1)


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['date_cmd', 'design_cmd', 'code_client']


