from django import forms
from .models import Impressora, Ramal, ThinClient
from patrimonios.models import Patrimonio


class ImpressoraForm(forms.ModelForm):
    class Meta:
        model = Impressora
        fields = ['ip', 'numero_equipamento',
                  'modelo', 'local', 'departamento']


class RamalForm(forms.ModelForm):
    class Meta:
        model = Ramal
        fields = ['usuario_ramal', 'senha', 'patrimonio', 'ramal', 'obs']


class ThinClientForm(forms.ModelForm):
    class Meta:
        model = ThinClient
        fields = ['patrimonio', 'usuario', 'senha',
                  'numero_monitor', 'departamento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patrimonio'].queryset = self.fields['patrimonio'].queryset.filter(
            tipo='THINCLIENT')
        self.fields['patrimonio'].label = "Número de Patrimônio (ThinClient)"
