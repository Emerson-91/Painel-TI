import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from dashboard.decorators import admin_required
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
from .models import Departamento, Local, Chamado, SequenciaChamado
from .forms import DepartamentoForm, LocalForm, ChamadoForm, EncerrarChamadoForm


@login_required
def abrir_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            chamado = form.save(commit=False)
            chamado.status = 'ABERTO'
            sequencia, _ = SequenciaChamado.objects.get_or_create(id=1)
            chamado.numero = sequencia.gerar_novo_numero()
            chamado.save()
            messages.success(request, f"Chamado Nr {
                             chamado.numero} aberto com sucesso!")
            return redirect('chamados')
    else:
        form = ChamadoForm()
    # Filtra apenas os departamentos e locais ativos
    form.fields['departamento'].queryset = Departamento.objects.filter(
        ativo=True)
    form.fields['local'].queryset = Local.objects.filter(ativo=True)
    return render(request, 'chamados/abrirChamados.html', {'form': form})


@admin_required
def cadastrar_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('configuracoes')
    else:
        form = DepartamentoForm()
    return render(request, 'chamados/cadastrar_departamento.html', {'form': form})


@admin_required
def cadastrar_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('configuracoes')
    else:
        form = LocalForm()
    return render(request, 'chamados/cadastrar_local.html', {'form': form})


@admin_required
def editar_departamento(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('configuracoes')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'chamados/editar_departamento.html', {'form': form})


@admin_required
def editar_local(request, pk):
    local = get_object_or_404(Local, pk=pk)
    if request.method == 'POST':
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return redirect('configuracoes')
    else:
        form = LocalForm(instance=local)
    return render(request, 'chamados/editar_local.html', {'form': form})


@admin_required
def ativar_departamento(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    departamento.ativo = True
    departamento.save()
    return redirect('configuracoes')


@admin_required
def ativar_local(request, pk):
    local = get_object_or_404(Local, pk=pk)
    local.ativo = True
    local.save()
    return redirect('configuracoes')


@admin_required
def desativar_departamento(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    departamento.ativo = False
    departamento.save()
    return redirect('configuracoes')


@admin_required
def desativar_local(request, pk):
    local = get_object_or_404(Local, pk=pk)
    local.ativo = False
    local.save()
    return redirect('configuracoes')


@login_required
def chamados_view(request):
    status_filter = request.GET.get('status', None)
    mes_atual = request.GET.get('mes_atual', None)
    quantidade_por_pagina = request.GET.get('quantidade', '10')

    hoje = timezone.now()
    inicio_do_mes = hoje.replace(
        day=1, hour=0, minute=0, second=0, microsecond=0)
    fim_do_mes = inicio_do_mes + relativedelta(months=1)

    if status_filter in ['ABERTO', 'FECHADO']:
        chamados = Chamado.objects.filter(status=status_filter)
    else:
        chamados = Chamado.objects.all()

    if mes_atual:
        chamados = chamados.filter(
            criado_em__gte=inicio_do_mes, criado_em__lt=fim_do_mes)

    # + para -
    chamados = chamados.order_by('-numero')

    # CALCULA O TEMPO DO CHAMADO
    for chamado in chamados:
        chamado.tempo_criacao_minutos = (
            timezone.now() - chamado.criado_em).total_seconds() / 60

    # Trata a opção 'todos'
    if quantidade_por_pagina == 'all':
        quantidade_por_pagina = chamados.count()
    else:
        try:
            quantidade_por_pagina = int(quantidade_por_pagina)
        except ValueError:
            quantidade_por_pagina = 10  # Fallback para o valor padrão se a conversão falhar

    # Paginação
    paginator = Paginator(chamados, quantidade_por_pagina)
    pagina_num = request.GET.get('pagina')

    try:
        pagina = paginator.get_page(pagina_num)
    except PageNotAnInteger:
        pagina = paginator.get_page(1)
    except EmptyPage:
        pagina = paginator.get_page(paginator.num_pages)

    user = request.user
    is_operador = user.groups.filter(name='Operador').exists()
    is_tecnico = user.groups.filter(name='Técnico').exists()
    is_administrador = user.groups.filter(name='Administrador').exists()

    context = {
        'chamados': pagina,
        'status_filter': status_filter,
        'mes_atual': mes_atual,
        'quantidade_por_pagina': quantidade_por_pagina,
        'paginator': paginator,
        'is_operador': is_operador,
        'is_tecnico': is_tecnico,
        'is_administrador': is_administrador,
    }

    return render(request, 'chamados/chamados.html', context)


@login_required
def encerrar_chamado(request, chamado_id):
    chamado = get_object_or_404(Chamado, id=chamado_id)

    # Verificar se o chamado já está encerrado
    if chamado.status == 'FECHADO':
        messages.error(
            request, "Este chamado já foi encerrado e não pode ser editado.")
        return redirect('visualizar_chamado', chamado_id=chamado.id)

    if request.method == 'POST':
        form = EncerrarChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            chamado = form.save(commit=False)
            chamado.status = 'FECHADO'
            chamado.encerrado_em = timezone.now()
            chamado.encerrado_por = request.user
            chamado.tempo_resposta = chamado.encerrado_em - chamado.criado_em
            chamado.save()
            messages.success(request, "Chamado encerrado com sucesso!")
            return redirect('chamados')
    else:
        # Inicializa o formulário com os dados existentes do chamado
        form = EncerrarChamadoForm(instance=chamado)

    return render(request, 'chamados/encerrar_chamado.html', {
        'form': form,
        'chamado': chamado
    })


@login_required
def visualizar_chamado(request, chamado_id):
    chamado = get_object_or_404(Chamado, id=chamado_id)
    user = request.user
    is_tecnico = user.groups.filter(name='Técnico').exists()
    is_administrador = user.groups.filter(name='Administrador').exists()
    context = {
        'chamado': chamado,
        'is_tecnico': is_tecnico,
        'is_administrador': is_administrador,
    }
    return render(request, 'chamados/visualizar_chamado.html', context)


@login_required
def chamados_encerrados_view(request):
    chamados_encerrados = Chamado.objects.filter(status='FECHADO')
    return render(request, 'chamados/chamados_encerrados.html', {'chamados': chamados_encerrados})


@login_required
def relatorios(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    tecnico = request.GET.get('tecnico', '')
    numero_chamado = request.GET.get('numero_chamado', '')
    patrimonio = request.GET.get('patrimonio', '')
    titulo = request.GET.get('titulo', '')
    departamento = request.GET.get('departamento', '')

    # FILTRO POR DATA
    if start_date:
        start_date = timezone.make_aware(
            timezone.datetime.strptime(start_date, '%Y-%m-%d'))
    else:
        start_date = timezone.make_aware(timezone.datetime.now().replace(
            year=2024, month=9, day=1, hour=0, minute=0, second=0, microsecond=0))

    if end_date:
        end_date = timezone.make_aware(timezone.datetime.strptime(
            end_date, '%Y-%m-%d')) + timezone.timedelta(days=1)
    else:
        end_date = timezone.make_aware(
            timezone.datetime.now() + timezone.timedelta(days=1))

    # Filtrar os chamados e ordenar
    chamados = Chamado.objects.filter(criado_em__range=(
        start_date, end_date)).order_by('criado_em')

    # FILTRO POR TÉCNICO
    if tecnico:
        chamados = chamados.filter(encerrado_por__username__icontains=tecnico)

    # FILTRO POR NÚMERO DE CHAMADO
    if numero_chamado:
        chamados = chamados.filter(numero=numero_chamado)

    # FILTRO POR NÚMERO DE PATRIMÔNIO
    if patrimonio:
        chamados = chamados.filter(nr_patrimonio__icontains=patrimonio)

    # FILTRO POR TÍTULO DE CHAMADO
    if titulo:
        chamados = chamados.filter(titulo__icontains=titulo)

    # FILTRO POR DEPARTAMENTO
    if departamento:
        chamados = chamados.filter(departamento__nome__icontains=departamento)

    # CHAMADOS POR TÉCNICO E POR PERÍODO
    chamados_por_tecnico = Chamado.objects.filter(
        status='FECHADO',
        criado_em__range=(start_date, end_date)
    ).values('encerrado_por__username').annotate(total_chamados=Count('id'))

    total_chamados = chamados.count()

    labels = [item['encerrado_por__username'] for item in chamados_por_tecnico]
    data = [item['total_chamados'] for item in chamados_por_tecnico]

    if request.GET.get('export_csv') == '1':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio_completo_chamados.csv"'

        response.write('\ufeff'.encode('utf8'))

        writer = csv.writer(response)

        # Cabeçalho do CSV
        writer.writerow([
            'Número do Chamado', 'Título', 'Descrição', 'Departamento', 'Local', 'Contato',
            'Status', 'Data de Criação', 'Data de Atualização', 'Data de Encerramento',
            'Técnico Responsável', 'Número de Patrimônio', 'Solução Técnica'
        ])

        # Escrevendo os dados de cada chamado
        for chamado in chamados:
            writer.writerow([
                chamado.numero,
                chamado.titulo,
                chamado.descricao,
                chamado.departamento.nome if chamado.departamento else 'N/A',
                chamado.local.nome if chamado.local else 'N/A',
                chamado.contato,
                chamado.status,
                chamado.criado_em.strftime('%Y-%m-%d %H:%M'),
                chamado.atualizado_em.strftime('%Y-%m-%d %H:%M'),
                chamado.encerrado_em.strftime(
                    '%Y-%m-%d %H:%M') if chamado.encerrado_em else 'N/A',
                chamado.encerrado_por.username if chamado.encerrado_por else 'N/A',
                chamado.nr_patrimonio,
                chamado.solucao_tecnica
            ])

        return response

    # Paginação
    paginator = Paginator(chamados, 10)  # 10 chamados por página
    page_number = request.GET.get('page')
    chamados_paginated = paginator.get_page(page_number)

    context = {
        'chamados': chamados_paginated,
        'total_chamados': total_chamados,
        'chamados_por_tecnico': chamados_por_tecnico,
        'labels': labels,
        'data': data,
        'start_date': start_date,
        'end_date': end_date,
        'current_month_start': timezone.make_aware(timezone.datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)),
        'current_month_end': timezone.make_aware(timezone.datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0) + timezone.timedelta(days=31)).replace(day=1),
        'tecnico': tecnico,
        'numero_chamado': numero_chamado,
        'patrimonio': patrimonio,
        'titulo': titulo,
        'departamento': departamento,
    }
    return render(request, 'chamados/relatorios.html', context)
