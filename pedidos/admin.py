from django.contrib import admin
from .models import Pedido, ItemPedido

# Inline para mostrar os itens dentro do Pedido
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1 

    fields = ("produto", "quantidade")

    readonly_fields = ()

# Configuração do Pedido no admin
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "forma_pagamento", "data_pedido", "data_entrega", "valor_total")
    list_filter = ("forma_pagamento", "data_pedido")

    search_fields = ("cliente__nome", "cliente__email")

    inlines = [ItemPedidoInline]

# Configuração do ItemPedido no admin (opcional, já aparece inline)
@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "produto", "quantidade", "subtotal")
