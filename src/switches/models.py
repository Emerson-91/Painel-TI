# switches/models.py
from django.db import models

class Switch(models.Model):
    nome = models.CharField(max_length=100) 
    local = models.CharField(max_length=100) 
    modelo = models.CharField(max_length=100) 
    numero_portas = models.IntegerField(choices=[(24, '24 portas'), (48, '48 portas'), (52, '52 portas')])
    poe = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(null=True, blank=False)

    def __str__(self):
        return self.nome

class PortaSwitch(models.Model):
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE, related_name="portas")
    numero_porta = models.PositiveIntegerField() 
    vlan = models.CharField(max_length=50)  
    destino = models.CharField(max_length=100)  
    localizacao = models.CharField(max_length=100)  # Localização física ou sala
    em_uso = models.BooleanField(default=False)

    def __str__(self):
        return f"Porta {self.numero_porta} - VLAN {self.vlan} ({self.destino})"