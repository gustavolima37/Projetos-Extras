from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('<int:id>/', views.detalhe_cliente, name='detalhe_clientes'),
]