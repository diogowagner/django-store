from django.contrib.admin import ModelAdmin, site

from loja.models import *

class CarrinhoAdmin(ModelAdmin):
    '''Personalizações de Administração para o Carrinho de Compras'''
    fields = ('cliente','fechado')

site.register(Carrinho, CarrinhoAdmin)