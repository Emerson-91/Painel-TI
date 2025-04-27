from django.db import models
from django.contrib.auth.models import User

class SequenciaChamado(models.Model):
    ultimo_numero = models.IntegerField(default=0)  # Armazena o último número gerado

    def gerar_novo_numero(self):
        self.ultimo_numero += 1
        self.save()
        return self.ultimo_numero

    def __str__(self):
        return f'Sequência de Chamados: {self.ultimo_numero}'

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)  # Indica se o departamento está ativo

    def __str__(self):
        return self.nome

class Local(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)  # Indica se o local está ativo

    def __str__(self):
        return self.nome
    
class Chamado(models.Model):
    STATUS_CHOICES = [
        ('ABERTO', 'Aberto'),
        ('FECHADO', 'Fechado'),
    ]
    
    TITULOS_CHOICES = [
        ('Computador', 'Computador'),
        ('Impressora', 'Impressora'),
        ('Telefone', 'Telefone'),
        ('Mudança','Mudança'),
        ('Outros', 'outros')
    ]
    
    numero = models.IntegerField(unique=True)
    titulo = models.CharField(max_length=100, choices=TITULOS_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True)
    contato = models.CharField(max_length=100)
    descricao = models.TextField()
    descricao_tecnica = models.TextField(null=True, blank=True) 
    solucao_tecnica = models.TextField(null=True, blank=True)
    nr_patrimonio = models.CharField(max_length=50, null=True, blank=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ABERTO')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    encerrado_em = models.DateTimeField(null=True, blank=True) 
    encerrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
    tempo_resposta = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.titulo