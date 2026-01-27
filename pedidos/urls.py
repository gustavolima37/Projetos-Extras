from django.urls import path
from . import views  # Isso importa o arquivo views.py que está na mesma pasta

urlpatterns = [
    # O caminho vazio '' significa que a URL será apenas /pedidos/
    path('', views.lista_pedidos, name='lista_pedidos'),
]