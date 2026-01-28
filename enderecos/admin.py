from django.contrib import admin
from . models import Endereco
# Register your models here.

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("rua", "numero", "cidade", "estado", "cliente")
    search_fields = ("rua", "cidade", "cliente__nome")
