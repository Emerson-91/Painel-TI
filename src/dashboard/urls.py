from django.urls import path, include
from .views import dashboard_view, configuracoes, register_user, edit_user, lista_logs_acesso, delete_user, pagina_sem_permissao

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('chamados/', include('chamados.urls')),
    path('configuracoes/', configuracoes, name='configuracoes'),
    path('register/', register_user, name='register_user'),
    path('edit/<int:user_id>/', edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('logs/acesso/', lista_logs_acesso, name='lista_logs_acesso'),
    path('SEM_PERMISSAO/', pagina_sem_permissao, name='pagina_sem_permissao'),

]
