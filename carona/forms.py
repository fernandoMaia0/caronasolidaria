from django import forms
from models.Carona import Carona  
from models.Endereco import Endereco

class CaronaForm(forms.ModelForm):
    class Meta:
        model = Carona
        fields = ['nome', 'horario', 'data', 'descricao', 'motorista', 'endereco_saida', 'endereco_destino', 'passageiros']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }


