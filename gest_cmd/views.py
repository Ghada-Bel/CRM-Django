
from django.shortcuts import render, get_object_or_404, redirect
from .models import Commande, Ligne_cmd
from .forms import LigneCmdFormSet,CommandeForm
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string



def edit_commande(request, commande_id):
    if request.user.is_authenticated:

        # Get the specific Commande instance
        commande_instance = get_object_or_404(Commande,num_cmd=commande_id)
        
        if request.method == "POST":
            # Initialize the formset with the POST data
            formset = LigneCmdFormSet(request.POST, instance=commande_instance)
            if formset.is_valid():
                # Save the formset
                formset.save()
                # Redirect to some view after saving
                return redirect('some_view_name')
        else:
            # Initialize an empty formset
            formset = LigneCmdFormSet(instance=commande_instance)
        
        # Render the formset in the template
        return render(request, 'gestion_cmd.html', {'formset': formset, 'commande': commande_instance})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('liste_commandes')


def add_formset_row(request, commande_id):
    commande_instance = get_object_or_404(Commande, num_cmd=commande_id)
    formset = LigneCmdFormSet(instance=commande_instance)
    new_form = formset.empty_form
    context = {'form': new_form}
    html = render_to_string('formset_row.html', context, request=request)
    return JsonResponse({'html': html})



def liste_commandes(request):
    if request.user.is_authenticated:
        # Fetch all Commande instances
        commandes = Commande.objects.all()
        return render(request, 'liste_commandes.html', {'commandes': commandes})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


def add_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_commandes')
    else:
        form = CommandeForm()
    return render(request, 'add_commande.html', {'form': form})

def delete_commande(request, commande_id):
    delete_it = Commande.objects.get(num_cmd=commande_id)
    delete_it.delete()
    messages.success(request, "Record Deleted Successfully...")
    return redirect('liste_commandes')
	
   
