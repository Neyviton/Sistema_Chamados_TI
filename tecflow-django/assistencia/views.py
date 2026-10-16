
# assistencia/views.py

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.db.models.deletion import ProtectedError

from .forms import ClienteForm
from .models import (
    Cliente,
    Equipamento,
    OrdemServico,
    Pagamento,
)


# Dashboard
def dashboard(request):
    contexto = {
        'titulo': 'Dashboard',
    }

    return render(request, 'assistencia/dashboard.html', contexto)


# Lista de clientes
def clientes_lista(request):
    pesquisa = request.GET.get('q', '').strip()

    clientes = Cliente.objects.all()

    if pesquisa:
        clientes = clientes.filter(
            Q(nome__icontains=pesquisa)
            | Q(telefone__icontains=pesquisa)
            | Q(email__icontains=pesquisa)
        )

    contexto = {
        'clientes': clientes,
    }

    return render(request, 'assistencia/clientes/lista.html', contexto)


# Cadastro de clientes
def cliente_criar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso.')
            return redirect('assistencia:clientes_lista')
    else:
        form = ClienteForm()

    contexto = {
        'titulo': 'Cadastrar cliente',
        'form': form,
    }

    return render(
        request,
        'assistencia/clientes/formulario.html',
        contexto,
    )


# Detalhes do cliente
def cliente_detalhes(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    contexto = {
        'cliente': cliente,
    }

    return render(
        request,
        'assistencia/clientes/detalhes.html',
        contexto,
    )


# Edição de clientes
def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso.')
            return redirect('assistencia:cliente_detalhes', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)

    contexto = {
        'titulo': 'Editar cliente',
        'cliente': cliente,
        'form': form,
    }

    return render(
        request,
        'assistencia/clientes/formulario.html',
        contexto,
    )


# Exclusão de clientes
@require_POST
def cliente_excluir(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    try:
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso.')
    except ProtectedError:
        messages.error(
            request,
            'Não foi possível excluir este cliente porque existem '
            'equipamentos vinculados a ele.',
        )

    return redirect('assistencia:clientes_lista')


# Lista de equipamentos
def equipamentos_lista(request):
    equipamentos = Equipamento.objects.select_related('cliente').all()

    contexto = {
        'equipamentos': equipamentos,
    }

    return render(
        request,
        'assistencia/equipamentos/lista.html',
        contexto,
    )


# Cadastro de equipamentos
def equipamento_criar(request):
    contexto = {
        'titulo': 'Cadastrar equipamento',
        'modo': 'criar',
    }

    return render(
        request,
        'assistencia/equipamentos/formulario.html',
        contexto,
    )


# Detalhes do equipamento
def equipamento_detalhes(request, pk):
    equipamento = get_object_or_404(
        Equipamento.objects.select_related('cliente'),
        pk=pk,
    )

    contexto = {
        'equipamento': equipamento,
    }

    return render(
        request,
        'assistencia/equipamentos/detalhes.html',
        contexto,
    )


# Edição de equipamentos
def equipamento_editar(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)

    contexto = {
        'titulo': 'Editar equipamento',
        'modo': 'editar',
        'equipamento': equipamento,
        'equipamento_id': pk,
    }

    return render(
        request,
        'assistencia/equipamentos/formulario.html',
        contexto,
    )


# Lista de ordens de serviço
def ordens_servico_lista(request):
    ordens_servico = OrdemServico.objects.select_related(
        'equipamento',
        'equipamento__cliente',
        'tecnico',
    ).all()

    contexto = {
        'ordens_servico': ordens_servico,
    }

    return render(
        request,
        'assistencia/ordens_servico/lista.html',
        contexto,
    )


# Cadastro de ordem de serviço
def ordem_servico_criar(request):
    contexto = {
        'titulo': 'Nova Ordem de Serviço',
        'modo': 'criar',
    }

    return render(
        request,
        'assistencia/ordens_servico/formulario.html',
        contexto,
    )


# Detalhes da ordem de serviço
def ordem_servico_detalhes(request, pk):
    ordem = get_object_or_404(
        OrdemServico.objects.select_related(
            'equipamento',
            'equipamento__cliente',
            'tecnico',
        ),
        pk=pk,
    )

    contexto = {
        'ordem': ordem,
    }

    return render(
        request,
        'assistencia/ordens_servico/detalhes.html',
        contexto,
    )


# Edição de ordem de serviço
def ordem_servico_editar(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)

    contexto = {
        'titulo': 'Editar Ordem de Serviço',
        'modo': 'editar',
        'ordem': ordem,
        'ordem_id': pk,
    }

    return render(
        request,
        'assistencia/ordens_servico/formulario.html',
        contexto,
    )


# Lista de pagamentos
def pagamentos_lista(request):
    pagamentos = Pagamento.objects.select_related(
        'ordem_servico',
        'ordem_servico__equipamento',
        'ordem_servico__equipamento__cliente',
    ).all()

    contexto = {
        'pagamentos': pagamentos,
    }

    return render(
        request,
        'assistencia/pagamentos/lista.html',
        contexto,
    )


# Cadastro de pagamento
def pagamento_criar(request):
    contexto = {
        'titulo': 'Registrar pagamento',
        'modo': 'criar',
    }

    return render(
        request,
        'assistencia/pagamentos/formulario.html',
        contexto,
    )


# Detalhes do pagamento
def pagamento_detalhes(request, pk):
    pagamento = get_object_or_404(
        Pagamento.objects.select_related(
            'ordem_servico',
            'ordem_servico__equipamento',
            'ordem_servico__equipamento__cliente',
        ),
        pk=pk,
    )

    contexto = {
        'pagamento': pagamento,
    }

    return render(
        request,
        'assistencia/pagamentos/detalhes.html',
        contexto,
    )


# Edição de pagamento
def pagamento_editar(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)

    contexto = {
        'titulo': 'Editar pagamento',
        'modo': 'editar',
        'pagamento': pagamento,
        'pagamento_id': pk,
    }

    return render(
        request,
        'assistencia/pagamentos/formulario.html',
        contexto,
    )
