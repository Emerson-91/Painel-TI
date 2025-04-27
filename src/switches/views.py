from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Switch, PortaSwitch
from .forms import SwitchForm, SwitchSearchForm, PortaSwitchForm

@login_required
def switches(request):
    form = SwitchSearchForm(request.GET or None)
    switches = Switch.objects.all()

    if form.is_valid():
        local = form.cleaned_data.get('local')
        ip = form.cleaned_data.get('ip')

        if local:
            switches = switches.filter(local__icontains=local)  # Filtra por local
        if ip:
            switches = switches.filter(ip=ip)  # Filtra por IP

    return render(request, 'switches/switches.html', {'form': form, 'switches': switches})
@login_required
def cadastro_switch(request):
    if request.method == 'POST':
        form = SwitchForm(request.POST)
        if form.is_valid():
            # Salva o Switch
            switch = form.save()

            # Cria as portas automaticamente de acordo com o número de portas do Switch
            numero_de_portas = switch.numero_portas  # 24 ou 48
            for numero_porta in range(1, numero_de_portas + 1):
                PortaSwitch.objects.create(
                    switch=switch,
                    numero_porta=numero_porta,
                    vlan='',  # Valor padrão para a VLAN
                    destino='',  # Valor padrão para o destino
                    localizacao='',  # Valor padrão para a localização
                    em_uso=False  # Valor padrão para 'em_uso'
                )

            # Redireciona para a lista de switches após salvar
            return redirect('switches')
    else:
        form = SwitchForm()

    return render(request, 'switches/cadastro_switch.html', {'form': form})

@login_required
def switch_detalhe(request, id):
    switch = get_object_or_404(Switch, id=id)

    return render(request, 'switches/switch_detalhe.html', {'switch': switch})
@login_required
def editar_switch(request, id):
    switch = get_object_or_404(Switch, id=id)
    
    if request.method == 'POST':
        form = SwitchForm(request.POST, instance=switch)
        if form.is_valid():
            form.save()
            return redirect('switch_detalhe', id=switch.id)  # Redireciona para a página de detalhes
    else:
        form = SwitchForm(instance=switch)

    return render(request, 'switches/editar_switch.html', {'form': form, 'switch': switch})

@login_required
def lista_portas(request):
    portas = PortaSwitch.objects.all()
    return render(request, 'switches/lista_portas.html', {'portas': portas})


@login_required
def editar_porta(request, id):
    porta = get_object_or_404(PortaSwitch, id=id)
    switch = porta.switch  # Obtendo o Switch relacionado à Porta

    if request.method == 'POST':
        form = PortaSwitchForm(request.POST, instance=porta)
        if form.is_valid():
            form.save()
            return redirect('lista_portas')
    else:
        form = PortaSwitchForm(instance=porta)

    return render(request, 'switches/editar_porta.html', {'form': form, 'porta': porta, 'switch': switch})
