from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_pedidos, name="lista_pedidos"),
    path("<int:id>/", views.detalhe_pedido, name="detalhe_pedido"),
]