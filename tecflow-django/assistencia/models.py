# fornece os tipos de campos e recurso do ORM do Django
from django.db import models
# Trabalha com valor monetário
from decimal import Decimal
#Informa que um dado não passou na validação
from django.core.exceptions import ValidationError
#define um valor mínimo para um campo
from django.core.validators import MinValueValidator
# Q: permite criar condições em consultas e restriçoes do banco
# Sum: calcula a soma de valores no banco de dados
from django.db.models import Q, Sum
#fornece date e hora de acordo com as configurações do django
from django.utils import timezone

#Criação do model Cliente
class Cliente(models.Model):
    
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255, blank=True)
    email =models.EmailField(blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordeing = ["nome"]
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome

# Criação do model Equipamento
class Equipamento(models.Model):
    class Tipo(models.TextChoices):
        CELULAR = "CELULAR", "Celular"
        NOTEBOOK = "NOTEBOOK", "Notebook"
        COMPUTADOR = "COMPUTADOR", "Computador"
        TELEVISAO = "TELEVISAO", "Televisão"
        OUTRO = "OUTRO", "Outro"

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="equipamentos",
    )
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["marca", "modelo"]
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"

    def __str__(self):
        return f"{self.marca} {self.modelo}"

#Criação do model Tecnico
class Tecnico(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"

    def __str__(self):
        return self.nome

# Criação model OrdemServico
class OrdemServico(models.Model):
    class Status(models.TextChoices):
        RECEBIDA = 'RECEBIDA', 'Recebida'
        EM_ANALISE = 'EM_ANALISE', 'Em análise'
        AGUARDANDO_APROVACAO = (
            "AGUARDANDO_APROVACAO",
            "Aguardando aprovação",
        )
        AGUARDANDO_PECAS = "AGUARDANDO_PECAS", "Aguardando peças"
        EM_REPARO = "EM_REPARO", "Em reparo"
        CONCLUIDA = "CONCLUIDA", "Concluída"
        ENTREGUE =  "ENTREGUE", "Entregue"
        CANCELADA = "CANCELADA", "Cancelada"
