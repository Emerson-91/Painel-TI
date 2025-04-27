from django.db import models
from django.contrib.auth.models import User


class LogAcesso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    acao = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.usuario} - {self.acao} - {self.data_hora}"
