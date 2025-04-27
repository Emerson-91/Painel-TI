from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Impressora, Ramal, ThinClient
from .forms import ImpressoraForm, RamalForm, ThinClientForm

@login_required
def utilitarios(request):
    return render(request, 'utilitarios.html')

##############################   IMPRESSORAS   ###############################
@login_required
def cadastro_impressora(request):
    if request.method == 'POST':
        form = ImpressoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('impressoras')
    else:
        form = ImpressoraForm()
    return render(request, 'cadastro_impressora.html', {'form': form})

@login_required
def editar_impressora(request, pk):
    impressora = get_object_or_404(Impressora, pk=pk)
    if request.method == 'POST':
        form = ImpressoraForm(request.POST, instance=impressora)
        if form.is_valid():
            form.save()
            return redirect('impressoras')
    else:
        form = ImpressoraForm(instance=impressora)
    return render(request, 'editar_impressora.html', {'form': form})

@login_required
def impressoras_view(request):
    query = request.GET.get('imp', '')  
    if query:
        impressoras = Impressora.objects.filter(
            numero_equipamento__icontains=query
        ) | Impressora.objects.filter(
            local__nome__icontains=query  
        )
    else:
        impressoras = Impressora.objects.all()
    return render(request, 'impressoras.html', {'impressoras': impressoras})

########################## MANUAIS  ##############################################
@login_required
def manuals_view(request):
    return render(request, 'manuals.html')

@login_required
def manual_abaris(request):
    return render(request, 'abaris.html')

@login_required
def manual_thinclient(request):
    return render(request, 'thinclients.html')

@login_required
def manual_pc(request):
    return render(request, 'computador.html')

@login_required
def manual_3cx(request):
    return render(request, '3cx.html')

@login_required
def manual_impressoras(request):
    return render(request, 'manual_impressoras.html')
########################## RAMAIS ##############################################
@login_required
def lista_ramais(request):
    query = request.GET.get('ram', '')  
    if query:
        ramais = Ramal.objects.filter(
            ramal__icontains=query
        ) | Ramal.objects.filter(
            usuario_ramal__icontains=query
        )
    else:
        ramais = Ramal.objects.all()
    return render(request, 'ramais.html', {'ramais': ramais})

@login_required
def novo_ramal(request):
    if request.method == 'POST':
        form = RamalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ramais')  
    else:
        form = RamalForm()
    return render(request, 'edita_ramal.html', {'form': form})

@login_required
def edita_ramal(request, ramal_id):
    ramal = get_object_or_404(Ramal, pk=ramal_id)
    if request.method == 'POST':
        form = RamalForm(request.POST, instance=ramal)
        if form.is_valid():
            form.save()
            return redirect('ramais')  
    else:
        form = RamalForm(instance=ramal)
    return render(request, 'edita_ramal.html', {'form': form})

######################### THINCLIENTS ############################################

def lista_thinclients(request):
    patrimonio_busca = request.GET.get('patrimonio', '')
    
    if patrimonio_busca:
        thinclients = ThinClient.objects.filter(patrimonio__numero_patrimonio__icontains=patrimonio_busca)
    else:
        thinclients = ThinClient.objects.all()
    
    return render(request, 'lista_thinclients.html', {'thinclients': thinclients, 'patrimonio_busca': patrimonio_busca})

def criar_editar_thinclient(request, thinclient_id=None):
    thinclient = get_object_or_404(ThinClient, id=thinclient_id) if thinclient_id else None

    if request.method == "POST":
        form = ThinClientForm(request.POST, instance=thinclient)
        if form.is_valid():
            form.save()
            return redirect('lista_thinclients')
    else:
        form = ThinClientForm(instance=thinclient)

    return render(request, 'criar_editar_thinclient.html', {'form': form, 'thinclient': thinclient})

def excluir_thinclient(request, thinclient_id):
    thinclient = get_object_or_404(ThinClient, id=thinclient_id)
    if request.method == "POST":
        thinclient.delete()
        return redirect('lista_thinclients')
    return render(request, 'excluir_thinclient.html', {'thinclient': thinclient})