from rest_framework import viewsets
from .models import Endereco
from .serializers import EnderecoSerializer

# Create your views here.
class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
