from django import forms
from .models import Produto, Cliente, Compra
from django.forms import ModelForm

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

