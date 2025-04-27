from django.db import models
from patrimonios.models import Patrimonio
from chamados.models import Local, Departamento


class Impressora(models.Model):
    ip = models.GenericIPAddressField(protocol='IPv4', unique=True)
    numero_equipamento = models.CharField(max_length=50, unique=True)
    modelo = models.CharField(max_length=100)
    # Relacionado ao modelo Local
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True)
    # Relacionado ao modelo Departamento
    departamento = models.ForeignKey(
        Departamento, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.modelo} - {self.numero_equipamento}"


class Ramal(models.Model):
    usuario_ramal = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    patrimonio = models.ForeignKey(
        Patrimonio,
        on_delete=models.CASCADE,
        limit_choices_to=models.Q(tipo='COMPUTADOR') | models.Q(
            tipo='TELEFONE'),  # Restringe a tipos 'COMPUTADOR' e 'TELEFONE'
        verbose_name="Número de Patrimônio"
    )
    ramal = models.CharField(max_length=20)
    obs = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario_ramal} - {self.ramal}"


class ThinClient(models.Model):
    patrimonio = models.ForeignKey(
        Patrimonio,
        on_delete=models.CASCADE,
        # Apenas patrimônios do tipo ThinClient
        limit_choices_to={'tipo': 'THINCLIENT'},
        verbose_name="Número de Patrimônio"
    )
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    numero_monitor = models.CharField(max_length=20)
    # Utilizando o modelo de chamados
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patrimonio} - {self.usuario}"
