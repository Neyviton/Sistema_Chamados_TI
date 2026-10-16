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
        ordering = ["nome"]
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

    class Prioridade(models.TextChoices):
        BAIXA = "BAIXA", "Baixa"
        NORMAL = "NORMAL", "Normal"
        ALTA = "ALTA", "Alta"
        URGENTE = "URGENTE", "Urgente"

    equipamento = models.ForeignKey(
        Equipamento,
        on_delete=models.PROTECT,
        related_name="ordens_servico"
    )

    tecnico = models.ForeignKey(
        Tecnico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ordens_servico",
    )

    descricao_problema = models.TextField()
    diagnostico = models.TextField(blank=True)
    status = models.CharField(
        max_length=25,
        choices=Status.choices, 
        default=Status.RECEBIDA,)

    prioridade = models.CharField(
        max_length=10,
        choices=Prioridade.choices,
        default=Prioridade.NORMAL,
    )

    orcamento = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    orcamento_aprovado = models.BooleanField(default=False)
    data_entrada = models.DateTimeField(default=timezone.now)
    data_previsao = models.DateTimeField(null=True, blank=True)
    data_saida = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-data_entrada"]
        verbose_name = "Ordem de serviço"
        verbose_name_plural = "Ordens de serviço"
        constraints = [
            models.CheckConstraint(
                condition=Q(orcamento__gt=0) | Q(orcamento__isnull=True),
                name= "ordem_orcamento_nao_negativo",
            ),
        ]

    def clean(self):
        super().clean()
        erros = {}

        if self.data_previsao and self.data_entrada:
            if self.data_previsao < self.data_entrada:
                erros["data_previsao"] = (
                    "A previsão não pode ser anterior à entrada."
                )

        if self.data_saida and self.data_entrada:
            if self.data_saida < self.data_entrada:
                erros["data_saida"] = (
                    "A saída não pode ser anterior à entrada"
                )

        status_final = {
            self.Status.CONCLUIDA,
            self.Status.ENTREGUE,
        }

        if self.status in status_final:
            if self.orcamento is None or not self.orcamento_aprovado:
                erros["orcamento_aprovado"] = (
                    "Informe um orçamento e registre sua aprovação "
                    "antes de concluir ou entregar o equipemento."
                )

        if erros:
            raise ValidationError(erros)

    def __str__(self):
        return f"OS #{self.pk} - {self.equipamento}"

# Criação model Pagamento
class Pagamento(models.Model):
    class FormaPagamento(models.TextChoices):
        DINHEIRO = "DINHEIRO", "Dinheiro"
        PIX = "PIX", "Pix"
        CREDITO = "CREDITO", "Cartão de crédito"
        DEBITO = "DEBITO", "Cartão de débito"
        OUTRO = "OUTRO", "Outro"

    ordem_servico = models.ForeignKey(
        OrdemServico,
        on_delete=models.PROTECT,
        related_name="pagamentos",
    )
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    data_pagamento = models.DateTimeField(default=timezone.now)
    forma_pagamento = models.CharField(
        max_length=10,
        choices=FormaPagamento.choices,
    )
    observacao = models.TextField(blank=True)

    class Meta:
        ordering = ["-data_pagamento"]
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"
        constraints = [
            models.CheckConstraint(
                condition=Q(valor__gt=0),
                name="pagamento_valor_maior_que_zero",
            ),
        ]

    def clean(self):
        super().clean()

        if not self.ordem_servico_id or self.valor is None:
            return

        ordem = self.ordem_servico

        if ordem.orcamento is None or not ordem.orcamento_aprovado:
            raise ValidationError({
                "ordem_servico": (
                    "A ordem precisa ter um orçamento aprovado "
                    "antes de receber pagamentos."
                )
            })

        pagamentos_anteriores = ordem.pagamentos.exclude(
            pk=self.pk
        ).aggregate(total=Sum("valor"))["total"] or Decimal("0.00")

        if pagamentos_anteriores + self.valor > ordem.orcamento:
            raise ValidationError({
                "valor": (
                    "A soma dos pagamentos não pode ultrapassar "
                    "o orçamento aprovado."
                )
            })

    def __str__(self):
        return f"Pagamento de R$ {self.valor} - OS #{self.ordem_servico_id}"