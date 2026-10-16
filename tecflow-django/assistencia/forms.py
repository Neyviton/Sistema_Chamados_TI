# assistencia/forms.py

from decimal import Decimal

from django import forms
from django.db.models import Q

from .models import Equipamento, OrdemServico, Pagamento, Tecnico


# Formatos enviados pelo campo datetime-local do navegador
FORMATOS_DATA_HORA = ['%Y-%m-%dT%H:%M', '%Y-%m-%dT%H:%M:%S']


# Campo de data e hora do navegador (o format permite preencher na edição)
def campo_data_hora():
    return forms.DateTimeInput(
        attrs={'class': 'form-control', 'type': 'datetime-local'},
        format=FORMATOS_DATA_HORA[0],
    )


# Formulário de equipamento baseado no model
class EquipamentoForm(forms.ModelForm):

    class Meta:
        model = Equipamento

        # Campos que serão exibidos no formulário
        fields = [
            'cliente',
            'tipo',
            'marca',
            'modelo',
            'numero_serie',
            'descricao',
        ]

        # Rótulos dos campos
        labels = {
            'cliente': 'Cliente',
            'tipo': 'Tipo de equipamento',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'numero_serie': 'Número de série',
            'descricao': 'Descrição',
        }

        # Aparência dos campos com Bootstrap
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Samsung',
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Galaxy A54',
            }),
            'numero_serie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe o número de série, se disponível',
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Cor, acessórios, estado físico...',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].empty_label = 'Selecione um cliente'
        self.fields['tipo'].choices = [
            ('', 'Selecione o tipo'),
            *Equipamento.Tipo.choices,
        ]


# Formulário de técnico
class TecnicoForm(forms.ModelForm):

    class Meta:
        model = Tecnico

        fields = [
            'nome',
            'email',
            'telefone',
            'especialidade',
            'ativo',
        ]

        labels = {
            'nome': 'Nome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'especialidade': 'Especialidade',
            'ativo': 'Técnico ativo',
        }

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo',
                'autofocus': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'nome@email.com',
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000',
                'type': 'tel',
            }),
            'especialidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Celulares, Notebooks',
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

    # O e-mail é único: a comparação ignora maiúsculas e minúsculas
    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()

        outros = Tecnico.objects.filter(email__iexact=email)
        if self.instance.pk:
            outros = outros.exclude(pk=self.instance.pk)

        if outros.exists():
            raise forms.ValidationError(
                'Já existe um técnico cadastrado com este e-mail.',
                code='unique',
            )

        return email


# Formulário de Ordem de Serviço
class OrdemServicoForm(forms.ModelForm):

    class Meta:
        model = OrdemServico

        fields = [
            'equipamento',
            'tecnico',
            'descricao_problema',
            'diagnostico',
            'status',
            'prioridade',
            'orcamento',
            'orcamento_aprovado',
            'data_entrada',
            'data_previsao',
            'data_saida',
        ]

        labels = {
            'equipamento': 'Equipamento',
            'tecnico': 'Técnico responsável',
            'descricao_problema': 'Descrição do problema',
            'diagnostico': 'Diagnóstico técnico',
            'status': 'Status da ordem',
            'prioridade': 'Prioridade',
            'orcamento': 'Valor do orçamento (R$)',
            'orcamento_aprovado': 'Orçamento aprovado pelo cliente',
            'data_entrada': 'Data de entrada',
            'data_previsao': 'Previsão de conclusão',
            'data_saida': 'Data de saída',
        }

        widgets = {
            'equipamento': forms.Select(attrs={'class': 'form-select'}),
            'tecnico': forms.Select(attrs={'class': 'form-select'}),
            'descricao_problema': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descreva o problema relatado pelo cliente...',
            }),
            'diagnostico': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Informe o diagnóstico, se já houver...',
            }),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'prioridade': forms.Select(attrs={'class': 'form-select'}),
            'orcamento': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0.01',
                'placeholder': '0,00',
            }),
            'orcamento_aprovado': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'data_entrada': campo_data_hora(),
            'data_previsao': campo_data_hora(),
            'data_saida': campo_data_hora(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Aceita o formato enviado pelo campo datetime-local
        for nome in ('data_entrada', 'data_previsao', 'data_saida'):
            self.fields[nome].input_formats = FORMATOS_DATA_HORA

        # Somente técnicos ativos recebem ordens; na edição, o técnico
        # já vinculado continua disponível mesmo que esteja inativo
        self.fields['tecnico'].queryset = Tecnico.objects.filter(
            Q(ativo=True) | Q(pk=self.instance.tecnico_id)
        )
        self.fields['tecnico'].empty_label = 'Não atribuído'

        self.fields['equipamento'].queryset = (
            Equipamento.objects.select_related('cliente')
        )
        self.fields['equipamento'].empty_label = 'Selecione um equipamento'

    # O banco exige orçamento maior que zero (ou vazio)
    def clean_orcamento(self):
        orcamento = self.cleaned_data.get('orcamento')

        if orcamento is not None and orcamento <= Decimal('0'):
            raise forms.ValidationError(
                'Informe um valor maior que zero ou deixe o campo vazio.'
            )

        return orcamento


# Formulário de Pagamento
class PagamentoForm(forms.ModelForm):

    class Meta:
        model = Pagamento

        fields = [
            'ordem_servico',
            'valor',
            'forma_pagamento',
            'data_pagamento',
            'observacao',
        ]

        labels = {
            'ordem_servico': 'Ordem de Serviço',
            'valor': 'Valor do pagamento (R$)',
            'forma_pagamento': 'Forma de pagamento',
            'data_pagamento': 'Data do pagamento',
            'observacao': 'Observações',
        }

        widgets = {
            'ordem_servico': forms.Select(attrs={'class': 'form-select'}),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0.01',
                'step': '0.01',
                'placeholder': '0,00',
            }),
            'forma_pagamento': forms.Select(attrs={'class': 'form-select'}),
            'data_pagamento': campo_data_hora(),
            'observacao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Informações adicionais sobre o pagamento...',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_pagamento'].input_formats = FORMATOS_DATA_HORA

        self.fields['ordem_servico'].queryset = (
            OrdemServico.objects.select_related('equipamento__cliente')
        )
        self.fields['ordem_servico'].empty_label = (
            'Selecione uma Ordem de Serviço'
        )
        self.fields['forma_pagamento'].choices = [
            ('', 'Selecione a forma'),
            *Pagamento.FormaPagamento.choices,
        ]
