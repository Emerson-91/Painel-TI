from django.contrib import admin
from .models import Impressora, Ramal, ThinClient


class ImpressoraAdmin(admin.ModelAdmin):
    list_display = ('ip', 'numero_equipamento', 'modelo', 'local',
                    'departamento')  # Campos a serem exibidos na lista
    # Campos que podem ser buscados
    search_fields = ('ip', 'numero_equipamento', 'modelo')
    ordering = ('modelo',)  # Ordena pela modelo


class RamalAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na lista
    list_display = ('usuario_ramal', 'ramal', 'patrimonio')
    # Campos que podem ser buscados
    search_fields = ('usuario_ramal', 'ramal', 'patrimonio')
    ordering = ('usuario_ramal',)  # Ordena pelo usuário do ramal


class ThinclientAdmin(admin.ModelAdmin):
    list_display = ('patrimonio', 'usuario', 'senha', 'numero_monitor',
                    'departamento')  # Campos a serem exibidos na lista
    search_fields = ('patrimonio', 'usuario', 'senha', 'numero_moniotr',
                     'departamento')  # Campos que podem ser buscados
    ordering = ('usuario',)  # Ordena pelo usuário do ramal


# Registrando os modelos no admin
admin.site.register(Impressora, ImpressoraAdmin)
admin.site.register(Ramal, RamalAdmin)
admin.site.register(ThinClient, ThinclientAdmin)
