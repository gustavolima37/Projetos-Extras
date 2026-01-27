from django.db import models

# Create your models here.
class Pedido (models.Model):
     # Definindo as opções para o campo de pagamento
    FORMA_PAGAMENTO_CHOICES =[
        ('PIX', 'Pix'),
        ('CARTAO_CREDITO', 'Cartão de Crédito'),
        ('CARTAO_DEBITO', 'Cartão de Débito'),
        ('DINHEIRO', 'Dinheiro'),
    ]
    cpf_cliente = models.CharField( max_length=11, verbose_name="CPF do Cliente")
    produto = models.CharField(max_length=100)
    quantidade= models.IntegerField()
    valor_encomenda = models.DecimalField(max_digits=10, decimal_places= 2)
    forma_pagamento = models.CharField(
        max_length=20, 
        choices=FORMA_PAGAMENTO_CHOICES,
        verbose_name="Forma de Pagamento"
    )
    data_pedido = models.DateField(auto_now_add=True) 
    data_entrega = models.DateField()

    def __str__(self):
        return f"Pedido {self.id} - {self.produto} ({self.cpf_cliente})"
        