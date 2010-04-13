# -*- encoding: utf-8 -*- 
from django.db import models

# Create your models here.
class Cliente(models.Model):
    '''Informações de clientes'''
    nome    = models.CharField(max_length=1000)
    email   = models.EmailField()
    email_alt = models.EmailField()
    telefone_res = models.CharField(max_length=25)
    telefone_com = models.CharField(max_length=25)
    telefone_cel = models.CharField(max_length=25)
    cidade = models.CharField(max_length=500)
    pais = models.CharField(max_length=500)
    estado = models.CharField(max_length=500)
    endereco = models.TextField(max_length=1500)