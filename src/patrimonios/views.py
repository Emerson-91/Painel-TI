from django.shortcuts import render, redirect, get_object_or_404
import csv
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Patrimonio
from utilitarios.models import Ramal
from .forms import PatrimonioForm
from django.contrib.auth.decorators import login_required


@login_required
def cadastrar_patrimonio(request):
    if request.method == 'POST':
        form = PatrimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patrimonios')
        else:
            print(form.errors)
    else:
        form = PatrimonioForm()
    return render(request, 'patrimonios/cadastrar_patrimonio.html', {'form': form})


@login_required
def patrimonios_view(request):
    query = request.GET.get('q', '')
    # Campo padrão de ordenação
    order_by = request.GET.get('order_by', 'numero_patrimonio')

    # Filtra os patrimônios com base na busca
    if query:
        patrimonios_list = Patrimonio.objects.filter(
            numero_patrimonio__icontains=query
        )

        # Caso a busca não traga resultados para numero_patrimonio, tenta buscar pelo tipo
        if not patrimonios_list.exists():
            patrimonios_list = Patrimonio.objects.filter(
                tipo__icontains=query
            )

        # Caso a busca não traga resultados para tipo, tenta buscar pelo nome do departamento
        if not patrimonios_list.exists():
            patrimonios_list = Patrimonio.objects.filter(
                # Assumindo que o nome do departamento é o campo "nome"
                departamento__nome__icontains=query
            )
    else:
        patrimonios_list = Patrimonio.objects.all()

    # Aplica a ordenação ao resultado filtrado
    patrimonios_list = patrimonios_list.order_by(order_by)

    # Paginação
    paginator = Paginator(patrimonios_list, 20)  # 20 patrimônios por página
    page_number = request.GET.get('page')
    patrimonios = paginator.get_page(page_number)

    return render(request, 'patrimonios/patrimonios.html', {
        'patrimonios': patrimonios,
        'order_by': order_by,
        'query': query
    })


@login_required
def visualizar_patrimonio(request, id):
    patrimonio = get_object_or_404(Patrimonio, id=id)
    ramais = Ramal.objects.filter(patrimonio=patrimonio)
    return render(request, 'patrimonios/visualizar_patrimonio.html', {'patrimonio': patrimonio, 'ramais': ramais})


@login_required
def editar_patrimonio(request, patrimonio_id):
    patrimonio = get_object_or_404(Patrimonio, id=patrimonio_id)

    if request.method == 'POST':
        form = PatrimonioForm(request.POST, instance=patrimonio)
        if form.is_valid():
            form.save()
            return redirect('patrimonios')
    else:
        form = PatrimonioForm(instance=patrimonio)

    return render(request, 'patrimonios/editar_patrimonio.html', {'form': form, 'patrimonio': patrimonio})


@login_required
def exportar_patrimonios_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=patrimonios.csv'

    response.write('\ufeff')
    writer = csv.writer(response)
    writer.writerow(['Número de Patrimônio', 'Marca', 'Tipo',
                    'Local', 'Departamento', 'Observação'])

    for patrimonio in Patrimonio.objects.all():
        writer.writerow([
            patrimonio.numero_patrimonio,
            patrimonio.marca,
            patrimonio.tipo,
            patrimonio.local.nome if patrimonio.local else '',
            patrimonio.departamento.nome if patrimonio.departamento else '',
            patrimonio.obs
        ])

    return response


@login_required
def exportar_computadores_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="computadores.csv"'

    response.write('\ufeff')
    writer = csv.writer(response)
    # Cabeçalho da planilha
    writer.writerow(['Número de Patrimônio', 'Marca', 'Tipo', 'Local', 'Departamento', 'Observação',
                    'Memória RAM', 'HD', 'Processador', 'Placa de Vídeo', 'Possui Headset', 'Possui Webcam'])

    computadores = Patrimonio.objects.filter(
        tipo='COMPUTADOR',
        memoria_ram__isnull=False,
        hd__isnull=False,
        processador__isnull=False,
        placa_video__isnull=False
    )

    for computador in computadores:
        writer.writerow([
            computador.numero_patrimonio,
            computador.marca,
            computador.tipo,
            computador.local,
            computador.departamento,
            computador.obs,
            computador.memoria_ram,
            computador.hd,
            computador.processador,
            computador.placa_video,
            'Sim' if computador.tem_headset else 'Não',
            'Sim' if computador.tem_webcam else 'Não'
        ])

    return response
