from django.db import models

# Create your models here.
class Automovel(models.Model):
    tipo = models.CharField(max_length=20)
    cor = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    leilao = models.CharField(max_length=20)
    f_pagamento = models.CharField(max_length=20)
    ano = models.CharField(max_length=20)
    km_rodado = models.CharField(max_length=20)

    def __str__(self):
        return self.modelo
