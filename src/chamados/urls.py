from django.urls import path
from .views import (
    abrir_chamado,
    chamados_view,
    relatorios,
    cadastrar_departamento,
    cadastrar_local,
    editar_departamento,
    editar_local,
    ativar_departamento,
    ativar_local,
    desativar_departamento,
    desativar_local,
    encerrar_chamado,
    visualizar_chamado,

)

urlpatterns = [
    path('abrir/', abrir_chamado, name='abrir_chamado'),
    path('<int:chamado_id>/encerrar/', encerrar_chamado, name='encerrar_chamado'),
    path('', chamados_view, name='chamados'),
    path('<int:chamado_id>/visualizar/', visualizar_chamado, name='visualizar_chamado'),
    path('relatorios/', relatorios, name='relatorios'),
    path('cadastrar_departamento/', cadastrar_departamento, name='cadastrar_departamento'),
    path('cadastrar_local/', cadastrar_local, name='cadastrar_local'),
    path('departamentos/<int:pk>/editar/', editar_departamento, name='editar_departamento'),
    path('locais/<int:pk>/editar/', editar_local, name='editar_local'),
    path('departamentos/<int:pk>/ativar/', ativar_departamento, name='ativar_departamento'),
    path('locais/<int:pk>/ativar/', ativar_local, name='ativar_local'),
    path('departamentos/<int:pk>/desativar/', desativar_departamento, name='desativar_departamento'),
    path('locais/<int:pk>/desativar/', desativar_local, name='desativar_local'),
]
