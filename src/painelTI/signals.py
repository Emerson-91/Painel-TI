import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

# Configurando o logger
access_logger = logging.getLogger('access_logger')

# Registrando o login
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    access_logger.info(f"Login: {user.username} from {get_client_ip(request)}")

# Registrando o logout
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    access_logger.info(f"Logout: {user.username} from {get_client_ip(request)}")


# Função auxiliar para obter o IP do cliente
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
