from django.shortcuts import render,  redirect, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import logout
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from chamados.models import Departamento, Local, Chamado
from .models import LogAcesso
from dashboard.decorators import admin_required


@login_required
def dashboard_view(request):
    user = request.user
    
    # Verifica as permissões do usuário
    is_tecnico = user.groups.filter(name='Técnico').exists()
    is_administrador = user.groups.filter(name='Administrador').exists()
    
    # Obtém os chamados
    chamados = Chamado.objects.all()
    total_chamados = chamados.count()
    chamados_abertos = chamados.filter(status='ABERTO').count()
    chamados_fechados = chamados.filter(status='FECHADO').count()
    
    # Filtros para chamados abertos
    chamados_abertos_detalhados = chamados.filter(status='ABERTO')
    
    # Saudação baseada no horário
    now = timezone.now()
    hora = now.hour

    if hora < 12:
        saudacao = "Bom dia"
    elif 12 <= hora < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"
    
    # Calcula o tempo de criação e tempo de resposta (se encerrado)
    for chamado in chamados_abertos_detalhados:
        chamado.tempo_criacao_minutos = (now - chamado.criado_em).total_seconds() / 60
        if chamado.encerrado_em:
            chamado.tempo_resposta = chamado.encerrado_em - chamado.criado_em
        else:
            chamado.tempo_resposta = None
    
    # Chamados encerrados por técnico
    chamados_por_tecnico = chamados.filter(status='FECHADO').values('encerrado_por__username').annotate(total_chamados=Count('id'))
    labels = [item['encerrado_por__username'] for item in chamados_por_tecnico]
    data = [item['total_chamados'] for item in chamados_por_tecnico]
         
    context = {
        'total_chamados': total_chamados,
        'chamados_abertos': chamados_abertos,
        'chamados_fechados': chamados_fechados,
        'chamados': chamados_abertos_detalhados,  # Somente chamados abertos detalhados
        'username': user.get_full_name() or user.username,  
        'saudacao': saudacao,
        'labels': labels,
        'data': data,
        'is_tecnico': is_tecnico,
        'is_administrador': is_administrador,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def configuracoes(request):
    user = request.user
    if not user.groups.filter(name='Administrador').exists():
        return redirect(reverse('pagina_sem_permissao'))

    users = User.objects.all()
    departamentos = Departamento.objects.all()
    locais = Local.objects.all()
    return render(request, 'dashboard/configuracoes.html', {
        'users': users,
        'departamentos': departamentos,
        'locais': locais,
    })


@admin_required
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.set(form.cleaned_data.get('groups'))
            messages.success(request, f"Usuario: {user} criado com sucesso!")
            return redirect('configuracoes')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register_user.html', {'form': form,})


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()  # Salva o usuário
            user.groups.set(form.cleaned_data.get('groups'))  # Atualiza os grupos do usuário
            return redirect('configuracoes')
    else:
        form = UserRegistrationForm(instance=user)  # Carrega o usuário atual para edição
    return render(request, 'registration/edit_user.html', {'form': form})

@admin_required
def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('configuracoes')
    return redirect('configuracoes')


class CustomLogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')
    
def pagina_sem_permissao(request):
    return render(request, 'dashboard/SEM_PERMISSAO.html')

@admin_required
def lista_logs_acesso(request):
    logs_list = LogAcesso.objects.all().order_by('-data_hora')
    paginator = Paginator(logs_list, 10)  # Mostra 10 logs por página
    page_number = request.GET.get('page')
    logs = paginator.get_page(page_number) 
    return render(request, 'dashboard/lista_logs_acesso.html', {'logs': logs})