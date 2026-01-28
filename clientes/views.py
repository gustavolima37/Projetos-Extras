from django.shortcuts import render, get_object_or_404
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})

def detalhe_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    enderecos = cliente.enderecos.all()

    return render(request, 'clientes/detalhe.html', {
        'cliente': cliente, 
        'enderecos': enderecos
        })