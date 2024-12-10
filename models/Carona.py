from django.db import models
from models.Usuario import Usuario
from models.Endereco import Endereco
from django.utils.timezone import now
 
class Carona(models.Model):
    nome = models.CharField(max_length=100)
    horario = models.TimeField()
    data = models.DateField(default=now)
    descricao = models.TextField(blank=True, null=True)
    motorista = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='caronas_oferecidas') #related name vai permitir acessar as caronas que ele já ofereceu
    passageiros = models.ManyToManyField(Usuario, related_name='caronas_pegas') # related names vai permitir acessar as caronas que o passageiro já pegou
    endereco_saida = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name='caronas_saida') #vai permitir acessar as caronas que partiram daquele endereço
    endereco_destino = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name='caronas_destino')# vai permitir acessar as caronas que tem aquele destino
    STATUS_CHOICES = [
    ('A', 'Aberto'), 
    ('F', 'Concluído'),
    ('C', 'Cancelado'),
        ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    class Meta:
        app_label = 'carona'

    def __str__(self):
        return f"{self.nome}  {self.passageiros}"