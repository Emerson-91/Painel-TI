from django.utils import timezone
from .models import LogAcesso

class LogAcessoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            # Verifica se já existe um log recente (por exemplo, nos últimos 5 minutos)
            recent_log_exists = LogAcesso.objects.filter(
                usuario=request.user,
                data_hora__gte=timezone.now() - timezone.timedelta(minutes=5)
            ).exists()

            if not recent_log_exists:
                LogAcesso.objects.create(
                    usuario=request.user,
                    ip_address=request.META.get('REMOTE_ADDR'),
                    acao=f"Acesso à página: {request.path}",
                    data_hora=timezone.now()
                )

        return response
