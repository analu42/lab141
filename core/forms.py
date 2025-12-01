from django import forms
from .models import Produto, Cliente, Compra, Usuario
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


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

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'cpf', 'nome_completo', 'email', 'password1', 'password2']