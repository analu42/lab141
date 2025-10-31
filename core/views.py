from django.shortcuts import render, redirect
from .models import Cliente, Compra, Produto
from .forms import ClienteForm, CompraForm, ProdutoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cadastro (request):
    return render(request, 'cadastro.html')

def carrinho (request):
    return render(request, 'carrinho.html')

def login (request):
    return render(request, 'login.html')

def catalogo (request):
    return render(request, 'catalogo.html')

def cliente(request):
    cliente = Cliente.objects.all()
    
    contexto = {
        'lista_cliente': cliente
    }

    return render(request, 'cliente.html', contexto)

def cadastro_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cliente')


    contexto = {
        'form':form
    }

    return render(request, 'cadastro_cliente.html', contexto)

def compra(request):
    compra = Compra.objects.all()

    contexto = {
        'lista_compra':compra
    }

    return render(request, 'compra.html', contexto)

def cadastro_compra(request):
    form =  CompraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('compra')
    contexto = {
        'form':form
    }

    return render(request, 'cadastro_compra.html', contexto)

def produto(request):
    produto = Produto.objects.all()

    contexto = {
        'lista_produto':produto
    }

    return render(request, 'produto.html', contexto)

def cadastro_produto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produto')
    contexto = {
        'form':form
    }

    return render(request, 'cadastro_produto.html',contexto)