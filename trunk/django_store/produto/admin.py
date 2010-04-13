from django.contrib.admin import ModelAdmin, site

from produto.models import *

class ProdutoAdmin(ModelAdmin):
    '''Personalizações de Administração para os Produtos'''
    fields = ('nome','descricao','dt_validade','pr_compra','pr_venda','pr_promocao')

site.register(Produto, ProdutoAdmin)