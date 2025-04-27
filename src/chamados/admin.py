from django.contrib import admin
from .models import Chamado, Departamento, Local

class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status')  
    search_fields = ('titulo', 'descricao')
    list_filter = ('status', 'departamento')
    actions = ['encerrar_chamados']

    fieldsets = (
        (None, {
            'fields': ('titulo', 'descricao', 'departamento', 'local', 'contato')
        }),
        ('Status', {
            'fields': ('status',) 
        }),
    )

    def encerrar_chamados(self, request, queryset):
        for chamado in queryset:
            chamado.status = 'encerrado'
            chamado.save()
        self.message_user(request, "Chamados selecionados foram encerrados.")
    encerrar_chamados.short_description = "Encerrar chamados selecionados"

admin.site.register(Chamado, ChamadoAdmin)
admin.site.register(Departamento)
admin.site.register(Local)
