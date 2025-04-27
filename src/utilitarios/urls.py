from django.urls import path
from .views import *
urlpatterns = [
    path('utilitarios', utilitarios, name='utilitarios'), 
    path('cadastro/',cadastro_impressora, name='cadastro_impressora'),
    path('editar/<int:pk>/', editar_impressora, name='editar_impressora'),
    path('impressoras/', impressoras_view, name='impressoras'),
    path('manuals/', manuals_view, name='manuals'),
    path('manuals/abaris/', manual_abaris, name='manual_abaris'),
    path('manuals/computador/', manual_pc, name='manual_pc'),
    path('manuals/3cx/', manual_3cx, name='manual_3cx'),
    path('manuals/manual_impressoras/', manual_impressoras, name='manual_impressoras'),
    path('manuals/manual_thinclient/', manual_thinclient, name='manual_thinclient'),
    path('ramais/', lista_ramais, name='ramais'),
    path('ramais/cadastrar/', novo_ramal, name='novo_ramal'),
    path('ramais/editar/<int:ramal_id>/', edita_ramal, name='edita_ramal'),
    path('thinclients/', lista_thinclients, name='lista_thinclients'),
    path('thinclients/novo/', criar_editar_thinclient, name='criar_thinclient'),
    path('thinclients/editar/<int:thinclient_id>/', criar_editar_thinclient, name='editar_thinclient'),
    path('thinclients/excluir/<int:thinclient_id>/', excluir_thinclient, name='excluir_thinclient'),
    
]