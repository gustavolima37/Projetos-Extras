from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def detalhe_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    enderecos = cliente.enderecos.all()

    return render(request, 'clientes/detalhe_clientes.html', {
        'cliente': cliente, 
        'enderecos': enderecos
        })