from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from loja import views

urlpatterns = patterns('',
    url(r'^$',                                          views.index,                        name='index'),
    url(r'^carrinho/$',                                 views.carrinho_ver,                 name='ver_carrinho'),
    url(r'^carrinho/add/(?P<id_produto>\d+)/$',         views.carrinho_add_produto,         name='add_produto_carrinho'),
    url(r'^carrinho/excluir/(?P<id_produto>\d+)/$',     views.carrinho_excluir_produto,     name='excluir_produto_carrinho'),
    url(r'^carrinho/concluir/$',                        views.carrinho_concluir,            name='concluir_carrinho'),
)
