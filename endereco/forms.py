from django import forms
  
from models.Endereco import Endereco

class enderecoForm(forms.ModelForm):
    class meta:
        model=Endereco
        fields='__all__'