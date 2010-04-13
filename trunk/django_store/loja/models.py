from django.db import models

from produto.models import Produto
from cliente.models import Cliente

# Create your models here.
class Carrinho(models.Model):
    '''Carrinho de compras'''
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    fechado = models.BooleanField()
    data = models.DateTimeField(auto_now=True)
    
class ItensCarrinho(models.Model):
    '''Itens do carrinho de compras'''
    produto = models.ForeignKey(Produto)
    carrinho = models.ForeignKey(Carrinho)
    quantidade = models.PositiveIntegerField()
    pr_total = models.FloatField()