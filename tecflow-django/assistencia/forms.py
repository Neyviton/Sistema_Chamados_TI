# assistencia/forms.py

from django import forms
from .models import Equipamento


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
            'cliente': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'tipo': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex.: Samsung',
                }
            ),
            'modelo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex.: Galaxy A54',
                }
            ),
            'numero_serie': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe o número de série',
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Descreva o equipamento...',
                }
            ),
        }

# assistencia/forms.py

from django import forms
from .models import Equipamento, OrdemServico


# Formulário de Ordem de Serviço baseado no model
class OrdemServicoForm(forms.ModelForm):

    class Meta:
        model = OrdemServico

        # Campos exibidos na tela
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

        # Rótulos dos campos
        labels = {
            'equipamento': 'Equipamento',
            'tecnico': 'Técnico responsável',
            'descricao_problema': 'Descrição do problema',
            'diagnostico': 'Diagnóstico técnico',
            'status': 'Status da ordem',
            'prioridade': 'Prioridade',
            'orcamento': 'Valor do orçamento (R$)',
            'orcamento_aprovado': 'Orçamento aprovado',
            'data_entrada': 'Data de entrada',
            'data_previsao': 'Previsão de conclusão',
            'data_saida': 'Data de saída',
        }

        # Widgets e classes visuais do Bootstrap
        widgets = {
            'equipamento': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'tecnico': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'descricao_problema': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Descreva o problema relatado pelo cliente...',
                }
            ),
            'diagnostico': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Informe o diagnóstico técnico...',
                }
            ),
            'status': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'prioridade': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'orcamento': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01',
                    'min': '0.01',
                    'placeholder': '0,00',
                }
            ),
            'orcamento_aprovado': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
            'data_entrada': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                }
            ),
            'data_previsao': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                }
            ),
            'data_saida': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                }
            ),
        }

# assistencia/forms.py

from django import forms
from .models import Equipamento, OrdemServico, Pagamento


# Formulário de equipamento
class EquipamentoForm(forms.ModelForm):

    class Meta:
        model = Equipamento
        fields = [
            'cliente',
            'tipo',
            'marca',
            'modelo',
            'numero_serie',
            'descricao',
        ]

        labels = {
            'cliente': 'Cliente',
            'tipo': 'Tipo de equipamento',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'numero_serie': 'Número de série',
            'descricao': 'Descrição',
        }

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
                'placeholder': 'Informe o número de série',
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva o equipamento...',
            }),
        }


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
            'orcamento_aprovado': 'Orçamento aprovado',
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
            }),
            'diagnostico': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'prioridade': forms.Select(attrs={'class': 'form-select'}),
            'orcamento': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0.01',
            }),
            'orcamento_aprovado': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'data_entrada': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
            'data_previsao': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
            'data_saida': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
        }


# Formulário de Pagamento
class PagamentoForm(forms.ModelForm):

    class Meta:
        model = Pagamento
        fields = [
            'ordem_servico',
            'valor',
            'data_pagamento',
            'forma_pagamento',
            'observacao',
        ]

        labels = {
            'ordem_servico': 'Ordem de Serviço',
            'valor': 'Valor do pagamento (R$)',
            'data_pagamento': 'Data do pagamento',
            'forma_pagamento': 'Forma de pagamento',
            'observacao': 'Observações',
        }

        widgets = {
            'ordem_servico': forms.Select(attrs={
                'class': 'form-select',
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0.01',
                'step': '0.01',
                'placeholder': '0,00',
            }),
            'data_pagamento': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
            'forma_pagamento': forms.Select(attrs={
                'class': 'form-select',
            }),
            'observacao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Informações adicionais sobre o pagamento...',
            }),
        }