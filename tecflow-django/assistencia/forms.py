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