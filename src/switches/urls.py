from django.urls import path
from .views import *



urlpatterns = [
    path('', switches, name='switches'), 
    path('novo/', cadastro_switch, name='cadastro_switch'),  # Cadastro de switch
    path('<int:id>/', switch_detalhe, name='switch_detalhe'),
    path('<int:id>/editar/', editar_switch, name='editar_switch'),
    path('portas/', lista_portas, name='lista_portas'),
    path('portas/editar/<int:id>/', editar_porta, name='editar_porta'),
]