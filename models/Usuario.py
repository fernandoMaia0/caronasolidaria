from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome_completo=models.CharField(max_length=200)
    cnh = models.CharField(max_length=20, blank=True, null=True)  # CNH só será usada por motoristas
    telefone = models.CharField(max_length=25)
    tem_carro = models.BooleanField(default=False)
    email=models.EmailField(max_length=100,blank=True,null=True,unique=True)
    senha = models.CharField(max_length=128)
    nome_usuario=models.CharField(unique=True,max_length=100)
    TIPO_USUARIO_CHOICES = [
        ('M', 'Motorista'),
        ('P', 'passageiro'),
    ]
    tipo_usuario=models.CharField(
        max_length=1,
        choices=TIPO_USUARIO_CHOICES,
        
        )
    class Meta:
        app_label = 'perfil' 

    def __str__(self):
        return self.nome_completo
