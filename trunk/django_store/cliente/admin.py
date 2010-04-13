from django.contrib.admin import ModelAdmin, site

from cliente.models import *

class ClienteAdmin(ModelAdmin):
    '''Personalizaçães de Administração para os Clientes'''
    fields = ('nome','email','email_alt','telefone_res','telefone_com','telefone_cel','cidade','pais','estado','endereco')

site.register(Cliente, ClienteAdmin)