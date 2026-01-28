from rest_framework import serializers
from .models import Cliente
from enderecos.models import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"

class ClienteSerializer(serializers.ModelSerializer):
    enderecos = EnderecoSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = ["id", "nome", "email", "enderecos"]