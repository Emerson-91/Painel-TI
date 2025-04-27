from django import forms
from .models import Switch, PortaSwitch

class SwitchForm(forms.ModelForm):
    class Meta:
        model = Switch
        fields = ['nome', 'local', 'modelo', 'numero_portas', 'ip', 'poe']

class SwitchSearchForm(forms.Form):
    local = forms.CharField(required=False, label='Local')
    ip = forms.GenericIPAddressField(required=False, label='IP')
    

class PortaSwitchForm(forms.ModelForm):
    class Meta:
        model = PortaSwitch
        fields = [ 'numero_porta', 'vlan', 'destino', 'localizacao', 'em_uso']