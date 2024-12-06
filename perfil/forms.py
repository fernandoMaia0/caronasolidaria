from django import forms
from models.Usuario import Usuario

class UsuarioForm(forms.ModelForm):
    confirma_senha= forms.CharField(max_length=255)
    class Meta:
        model = Usuario
        fields = '__all__'  
        widgets = {
            'senha': forms.PasswordInput(),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome_completo': 'Nome Completo',
            'nome_usuario': 'Nome de Usuário',
            'email': 'Email',
            'telefone': 'Telefone',
            'cnh': 'CNH (opcional)',
            'tem_carro': 'Possui Carro?',
            'tipo_usuario': 'Tipo de Usuário',
            'senha': 'Senha',
        }
    def clean_email(self):
     email = self.cleaned_data.get("email")  # Obtém o e-mail do formulário
     if Usuario.objects.filter(email=email).exists():  # Verifica se já existe no banco
      raise forms.ValidationError("Este e-mail já está cadastrado.")  # Lança um erro
     return email  # Retorna o e-mail
    
    def clean_confirma_senha(self):
            cleaned_data=super().clean()
            senha = self.cleaned_data.get("senha")
            confirma_senha = self.cleaned_data.get("confirma_senha")
            if  senha!= confirma_senha:
                raise forms.ValidationError("As senhas não coincidem. Por favor, tente novamente.")
            return cleaned_data
