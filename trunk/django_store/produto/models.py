from django.db import models

# Create your models here.
class Atributo(models.Model):
    '''Atributos configuraveis para os produtos'''
    nome = models.CharField(max_length=100)
    
class Produto(models.Model):
    '''Produtos da loja'''
    nome = models.CharField(max_length=300)
    descricao = models.TextField(max_length=6000)
    dt_validade = models.DateField()
    pr_compra = models.FloatField()
    pr_venda = models.FloatField()
    pr_promocao = models.FloatField()

class ImagemProduto(models.Model):
    '''Imagens de um produto e seu thumbnail'''
    produto = models.ForeignKey(Produto)
    imagem = models.ImageField(upload_to='PRD_IMGS')
    thumb = models.ImageField(upload_to='PRD_IMGS/THUMB')
    
class AtributoProduto(models.Model):
    '''Valor definido de cada atributo para um produto '''
    produto = models.ForeignKey(Produto)
    atributo = models.ForeignKey(Atributo)
    valor = models.CharField(max_length=2000)