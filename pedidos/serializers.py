from rest_framework import serializers
from .models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido 
        fields = '__all__' # Indica que todos os campos do modelo devem ser usadoscls