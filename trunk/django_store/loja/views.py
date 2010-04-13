# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response

def index(request):
    return render_to_response('index.html')
    
def carrinho_ver(request):
    return render_to_response('index.html')

def carrinho_add_produto(request, id_produto):
    return render_to_response('index.html')

def carrinho_excluir_produto(request, id_produto):
    return render_to_response('index.html')

def carrinho_concluir(request):
    return render_to_response('index.html')
