from django.db import models
from django.contrib.auth.models import AbstractUser

class Produto (models.Model):
    nome = models.CharField('Nome', 
                            max_length=50)
    preço = models.DecimalField('Preço', 
                               max_digits=10, 
                               decimal_places=2)
    largura = models.DecimalField('Largura', 
                                 max_digits=5, 
                                 decimal_places=2)
    altura = models.DecimalField('Altura', 
                                max_digits=5,
                                decimal_places=2)
    profundidade = models.DecimalField('Profundidade', 
                                   max_digits=5, 
                                   decimal_places=2)
    compra = models.ForeignKey('Compra', 
                               on_delete=models.PROTECT)

class Cliente(models.Model):
    nome = models.CharField('Nome', 
                            max_length=100)
    cpf = models.CharField('CPF', 
                           max_length=14,
                            primary_key=True)
    data_de_nascimento = models.DateField('Data de Nascimento')
    email = models.EmailField('E-mail', 
                              max_length=254)
    telefone = models.CharField('Telefone', 
                                max_length=15)
    endereco = models.TextField('Endereço')
    senha = models.CharField('Senha', 
                             max_length=50)
    
class Compra(models.Model):
    data_da_compra = models.DateField('Data da Compra')
    cliente = models.ForeignKey(Cliente, 
                                on_delete=models.PROTECT)
    
# Create your models here.
class Usuario(AbstractUser):
    cpf = models.CharField('CPF', max_length=11)
    nome_completo =  models.CharField('Nome Completo', max_length=50)
