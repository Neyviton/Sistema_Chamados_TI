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