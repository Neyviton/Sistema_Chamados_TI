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

