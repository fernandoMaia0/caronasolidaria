from django.db import models

class Endereco(models.Model):
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)  # Ex.: 'SP', 'RJ'
    rua = models.CharField(max_length=255)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"
