from django import forms
from .models import Patrimonio

class PatrimonioForm(forms.ModelForm):
    class Meta:
        model = Patrimonio
        fields = ['numero_patrimonio', 'marca', 'tipo', 'local', 'departamento', 'obs', 
                  'memoria_ram', 'hd', 'processador', 'placa_video', 'tem_headset', 'tem_webcam']

        widgets = {
            'tem_headset': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tem_webcam': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
