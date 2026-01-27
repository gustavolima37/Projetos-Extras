from django.shortcuts import render
from rest_framework import viewsets
from .models import Pedido
from .serializers import PedidoSerializer

# Create your views here.

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    # Aqui o Django vai buscar na sua pasta de templates global
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})