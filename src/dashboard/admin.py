from django.contrib import admin
from django.contrib.auth.models import User
from .models import LogAcesso

class LogAcessoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_hora', 'ip_address', 'acao')  # Campos a serem exibidos na lista
    search_fields = ('usuario__username', 'acao', 'ip_address')  # Permite buscar por usuário, ação e IP
    list_filter = ('usuario', 'acao')  # Permite filtrar por usuário e ação
    ordering = ('-data_hora',)  # Ordena por data/hora, do mais recente para o mais antigo

admin.site.register(LogAcesso, LogAcessoAdmin)
