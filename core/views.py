from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def manoel(request):
    return render(request, 'manoel.html')

def perfil(request):
    return render(request, 'perfil.html')