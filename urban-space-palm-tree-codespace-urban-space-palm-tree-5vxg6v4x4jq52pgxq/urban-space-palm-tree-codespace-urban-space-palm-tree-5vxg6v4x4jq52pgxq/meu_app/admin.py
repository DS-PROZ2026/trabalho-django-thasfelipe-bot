from django.contrib import admin
from .models import Equipamento


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "numero_patrimonio", "tipo", "em_uso")
    list_filter = ("em_uso", "tipo")
    search_fields = ("nome", "tipo", "numero_patrimonio")
