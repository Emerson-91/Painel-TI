from django.contrib import admin
from .models import Patrimonio

class PatrimonioAdmin(admin.ModelAdmin):
    list_display = ('numero_patrimonio', 'marca', 'tipo', 'local', 'departamento', 'obs')  # Campos a serem exibidos na lista
    search_fields = ('numero_patrimonio', 'marca', 'tipo', 'obs')  # Campos que podem ser buscados
    list_filter = ('tipo', 'local', 'departamento')  # Permite filtrar por tipo, local e departamento
    ordering = ('numero_patrimonio',)  # Ordena pela numeração de patrimônio

admin.site.register(Patrimonio, PatrimonioAdmin)
