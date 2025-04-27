from django.urls import path
from .views import patrimonios_view, cadastrar_patrimonio, editar_patrimonio,visualizar_patrimonio,exportar_computadores_csv, exportar_patrimonios_csv

urlpatterns = [
    path('', patrimonios_view, name='patrimonios'),
    path('cadastrar/', cadastrar_patrimonio, name='cadastrar_patrimonio'),
    path('visualizar/<int:id>/', visualizar_patrimonio, name='visualizar_patrimonio'),
    path('editar/<int:patrimonio_id>/', editar_patrimonio, name='editar_patrimonio'),
    path('exportar/csv/', exportar_patrimonios_csv, name='exportar_patrimonios_csv'),
    path('exportar/computadores/csv/', exportar_computadores_csv, name='exportar_computadores_csv'), 


]
