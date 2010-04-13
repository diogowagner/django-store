from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from cliente import views

urlpatterns = patterns('',
    url(r'^$',              views.listar,                   name='listar_cliente'),
    url(r'^novo/$',         login_required(views.novo),     name='novo_cliente'),
    url(r'^salvar/$',       login_required(views.salvar),   name='salvar_cliente'),
    url(r'^excluir/$',      login_required(views.excluir),  name='excluir_cliente'),
    url(r'^consultar/$',    views.consultar,                name='consultar_cliente'),
)
