from django.contrib import admin
# models importados
from .models import (
    Cliente,
    Equipamento,
    Tecnico,
    OrdemServico,
    Pagamento,
)

# Registro dos models

# Registro do model Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "telefone", "email", "data_cadastro")
    search_fields = ("nome", "telefone", "email")

# Registro do model Equipamento
@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ("id", "marca", "modelo", "tipo", "cliente")
    list_filter = ("tipo", "marca")
    search_fields = ("marca", "modelo", "numero_serie", "cliente__nome")
    list_select_related = ("cliente",)

# Registro do model Tecnico
@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "especialidade", "ativo")
    list_filter = ("ativo", "especialidade")
    search_fields = ("nome", "email")

# Registro do model OrdemServico
@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "equipamento",
        "tecnico",
        "status",
        "prioridade",
        "orcamento",
        "data_entrada",
    )
    list_filter = ("status", "prioridade", "orcamento_aprovado")
    search_fields = (
        "equipamento__marca",
        "equipamento__modelo",
        "equipamento__cliente__nome",
    )
    list_select_related = ("equipamento", "tecnico")

# Registro do model Pagamento
@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ordem_servico",
        "valor",
        "forma_pagamento",
        "data_pagamento",
    )
    list_filter = ("forma_pagamento",)
    list_select_related = ("ordem_servico",)