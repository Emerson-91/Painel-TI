from django import forms
from .models import Departamento, Local, Chamado


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nome']


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome']


class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['titulo', 'contato', 'descricao', 'departamento', 'local']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'local': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departamento'].queryset = Departamento.objects.filter(ativo=True)
        self.fields['local'].queryset = Local.objects.filter(ativo=True)


class EncerrarChamadoForm(forms.ModelForm):
    descricao_tecnica = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        label='Descrição Técnica',
        required=True
    )
    solucao_tecnica = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        label='Solução Técnica',
        required=True
    )
    nr_patrimonio = forms.CharField(
        label='Número de Patrimônio',
        required=True
    )

    class Meta:
        model = Chamado
        fields = [
            'titulo', 'numero', 'departamento', 'local', 'contato',
            'descricao', 'descricao_tecnica', 'solucao_tecnica', 'nr_patrimonio'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configurar os campos do formulário
        self.fields['titulo'].disabled = True
        self.fields['numero'].disabled = True
        self.fields['departamento'].disabled = True
        self.fields['local'].disabled = True
        self.fields['descricao'].disabled = True
        
        # Inicializar o campo 'contato' com o valor atual, mantendo-o editável
        if self.instance and self.instance.contato:
            self.fields['contato'].initial = self.instance.contato
