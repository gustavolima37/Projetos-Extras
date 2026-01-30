from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

# -----------------------
# Model Pedido
# -----------------------

class Pedido (models.Model):
     # Definindo as opções para o campo de pagamento
    FORMA_PAGAMENTO_CHOICES =[
        ('PIX', 'Pix'),
        ('CARTAO_CREDITO', 'Cartão de Crédito'),
        ('CARTAO_DEBITO', 'Cartão de Débito'),
        ('DINHEIRO', 'Dinheiro'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="pedidos",
        null=True, blank=True
    )

    produtos = models.ManyToManyField(
        Produto,
        through="ItemPedido", # tabela intermedária
        related_name="pedidos"
    )

    forma_pagamento = models.CharField(
        max_length=20,
        choices=FORMA_PAGAMENTO_CHOICES,
        verbose_name="Forma de Pagamento"
    )
    data_pedido = models.DateField(auto_now_add=True)
    data_entrega = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_total(self):
        total = sum(item.subtotal() for item in self.itens.all())
        self.valor_total = total
        self.save()
        return total
    
    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nome}"
    

# -----------------------
# Model ItemPedido (Tabela intermediária)
# -----------------------

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.produto.preco * self.quantidade
    
    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} (Pedido {self.pedido.id})"