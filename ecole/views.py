from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.


def description_create_view(request):
    form = descriptionForm()
    if request.method == 'POST':
        form = descriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_ligne_description')
            
    return render(request, 'ecole/description_list.html', {'form': form})


def load_niveaux(request):
    ecole_id = request.GET.get('ecole_id')
    niveaux = Niveau.objects.filter(ecole_id=ecole_id).all()
    
    return render(request, 'ecole/niveau_dropdown_list_options.html', {'niveaux': niveaux})

def load_classe(request):
    niveau_id = request.GET.get('niveau_id')
    classes = Classe.objects.filter(niveau_id=niveau_id).all()
    
    return render(request, 'ecole/classes_dropdown_list_options.html', {'classes': classes})


def list_ligne_description(request):
    descriptions=Description.objects.all()
    for d in descriptions:
        print(d.niveau_id)
    
    description_query=request.GET.get('description_text')
    ecole_query=request.GET.get('ecole_id')
    niveau_query=request.GET.get('niveau_id')
      

    if description_query:
        descriptions=descriptions.filter(description__icontains=description_query)
    elif ecole_query:
        descriptions=descriptions.filter(ecole__name=ecole_query)
    elif niveau_query:
        descriptions=descriptions.filter(niveau__name=niveau_query)
    
    ##elif description_query and ecole_query and niveau_query:
      ##  descriptions=descriptions.filter(Q(description__icontains=description_query) & Q(niveau__name=niveau_query) & Q(ecole__name=ecole_query))
       
                     
    



    context = {
        'descriptions':descriptions,
        
    }

    return render(request, 'ecole/list.html', context)