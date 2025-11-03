"""
URL configuration for lab141 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import index, cadastro, carrinho, login, catalogo,cliente, compra, produto, cadastro_cliente, cadastro_compra,cadastro_produto, atualizar_cliente, atualizar_compra, atualizar_produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('carrinho/', carrinho, name='carrinho'),
    path('login/', login, name='login'),
    path('catalogo/', catalogo, name='catalogo'),
    path('cliente/', cliente, name='cliente'),
    path('compra/', compra, name='compra'),
    path('produto/', produto, name='produto'),
    path('cadastro_cliente/', cadastro_cliente, name='cadastro_cliente'),
    path('cadastro_compra/', cadastro_compra, name='cadastro_compra'),
    path('cadastro_produto/', cadastro_produto, name='cadastro_produto'),
    path('atualizar_produto/<int:id>/', atualizar_produto, name='atualizar_produto'),
    path('atualizar_cliente/<str:cpf>/', atualizar_cliente, name='atualizar_cliente'),
    path('atualizar_compra/<int:id>/', atualizar_compra, name='atualizar_compra'),
]
