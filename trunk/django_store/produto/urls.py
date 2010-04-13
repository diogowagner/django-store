from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from produto import views

urlpatterns = patterns('',
    url(r'^$',              views.listar,                   name='listar_produto'),
    url(r'^novo/$',         login_required(views.novo),     name='novo_produto'),
    url(r'^salvar/$',       login_required(views.salvar),   name='salvar_produto'),
    url(r'^excluir/$',      login_required(views.excluir),  name='excluir_produto'),
    url(r'^consultar/$',    views.consultar,                name='consultar_produto'),
)
