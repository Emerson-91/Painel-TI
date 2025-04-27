from django.db import models
from chamados.models import Local, Departamento  # Importando de chamados

class Patrimonio(models.Model):
    TIPO_CHOICES = [
        ('CAMERA', 'Camera'),
        ('COMPUTADOR', 'Computador'),
        ('HEADSET', 'Headset'),
        ('IMPRESSORA', 'Impressora'),
        ('MONITOR', 'Monitor'),
        ('NOBREAK', 'Nobreak'),
        ('OUTROS', 'Outros'),
        ('RACK', 'Rack'),
        ('SWITCH', 'Switch'),
        ('TELEFONE', 'Telefone'),
        ('THINCLIENT', 'Thinclient'),
        ('WEBCAM', 'Webcam'),
        ('WIFI', 'Wifi')
        
    ]
    
    numero_patrimonio = models.CharField(max_length=50, unique=True)
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)  
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)  
    obs = models.CharField(max_length=50, blank=True)
    # Campos adicionais para computador
    memoria_ram = models.CharField(max_length=50, null=True, blank=True)
    hd = models.CharField(max_length=50, null=True, blank=True)
    processador = models.CharField(max_length=100, null=True, blank=True)
    placa_video = models.CharField(max_length=100, null=True, blank=True)

    # Campos para headset e webcam
    tem_headset = models.BooleanField(default=False, verbose_name="Possui Headset?")
    tem_webcam = models.BooleanField(default=False, verbose_name="Possui Webcam?")
    
    def __str__(self):
        return f"{self.numero_patrimonio} - {self.tipo}"
    
    
