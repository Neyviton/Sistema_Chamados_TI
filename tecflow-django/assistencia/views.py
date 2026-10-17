
# Importações
from django.contrib import messages
from django.db.models import Q
from django.db.models.deletion import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import (
    ClienteForm,
    EquipamentoForm,
    OrdemServicoForm,
    PagamentoForm,
)
from .models import Cliente, Equipamento, OrdemServico, Pagamento


# =========================
# DASHBOARD
# =========================

def dashboard(request):
    return render(request, 'assistencia/dashboard.html')


# =========================
# CLIENTES
# =========================

def clientes_lista(request):
    termo = request.GET.get('q', '').strip()
    clientes = Cliente.objects.all().order_by('nome')

    if termo:
        clientes = clientes.filter(
            Q(nome__icontains=termo)
            | Q(telefone__icontains=termo)
            | Q(email__icontains=termo)
        )

    return render(
        request,
        'assistencia/clientes/lista.html',
        {'clientes': clientes},
    )


def cliente_criar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('assistencia:clientes_lista')
    else:
        form = ClienteForm()

    return render(
        request,
        'assistencia/clientes/formulario.html',
        {'titulo': 'Cadastrar cliente', 'form': form},
    )


def cliente_detalhes(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    return render(
        request,
        'assistencia/clientes/detalhes.html',
        {'cliente': cliente},
    )


def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect(
                'assistencia:cliente_detalhes',
                pk=cliente.pk,
            )
    else:
        form = ClienteForm(instance=cliente)

    return render(
        request,
        'assistencia/clientes/formulario.html',
        {
            'titulo': 'Editar cliente',
            'cliente': cliente,
            'form': form,
        },
    )


@require_POST
def cliente_excluir(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    try:
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
    except ProtectedError:
        messages.error(
            request,
            'Não é possível excluir este cliente porque existem '
            'equipamentos vinculados a ele.',
        )

    return redirect('assistencia:clientes_lista')


# =========================
# EQUIPAMENTOS
# =========================

def equipamentos_lista(request):
    termo = request.GET.get('q', '').strip()

    equipamentos = Equipamento.objects.select_related(
        'cliente'
    ).all().order_by('-pk')

    if termo:
        equipamentos = equipamentos.filter(
            Q(cliente__nome__icontains=termo)
            | Q(tipo__icontains=termo)
            | Q(marca__icontains=termo)
            | Q(modelo__icontains=termo)
            | Q(numero_serie__icontains=termo)
        )

    return render(
        request,
        'assistencia/equipamentos/lista.html',
        {'equipamentos': equipamentos},
    )


def equipamento_criar(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)

        if form.is_valid():
            equipamento = form.save()
            messages.success(
                request,
                'Equipamento cadastrado com sucesso!',
            )
            return redirect(
                'assistencia:equipamento_detalhes',
                pk=equipamento.pk,
            )
    else:
        form = EquipamentoForm()

    return render(
        request,
        'assistencia/equipamentos/formulario.html',
        {
            'titulo': 'Cadastrar equipamento',
            'modo': 'criar',
            'form': form,
        },
    )


def equipamento_detalhes(request, pk):
    equipamento = get_object_or_404(
        Equipamento.objects.select_related('cliente'),
        pk=pk,
    )

    return render(
        request,
        'assistencia/equipamentos/detalhes.html',
        {'equipamento': equipamento},
    )


def equipamento_editar(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)

    if request.method == 'POST':
        form = EquipamentoForm(
            request.POST,
            instance=equipamento,
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Equipamento atualizado com sucesso!',
            )
            return redirect(
                'assistencia:equipamento_detalhes',
                pk=equipamento.pk,
            )
    else:
        form = EquipamentoForm(instance=equipamento)

    return render(
        request,
        'assistencia/equipamentos/formulario.html',
        {
            'titulo': 'Editar equipamento',
            'modo': 'editar',
            'equipamento': equipamento,
            'form': form,
        },
    )


@require_POST
def equipamento_excluir(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)

    try:
        equipamento.delete()
        messages.success(
            request,
            'Equipamento excluído com sucesso!',
        )
        return redirect('assistencia:equipamentos_lista')

    except ProtectedError:
        messages.error(
            request,
            'Não é possível excluir este equipamento porque ele '
            'está vinculado a uma ordem de serviço.',
        )
        return redirect(
            'assistencia:equipamento_detalhes',
            pk=equipamento.pk,
        )


# =========================
# ORDENS DE SERVIÇO
# =========================

def ordens_servico_lista(request):
    termo = request.GET.get('q', '').strip()

    ordens = OrdemServico.objects.select_related(
        'equipamento',
        'equipamento__cliente',
        'tecnico',
    ).all().order_by('-pk')

    if termo:
        ordens = ordens.filter(
            Q(equipamento__cliente__nome__icontains=termo)
            | Q(equipamento__marca__icontains=termo)
            | Q(equipamento__modelo__icontains=termo)
            | Q(descricao_problema__icontains=termo)
            | Q(status__icontains=termo)
        )

    return render(
        request,
        'assistencia/ordens/lista.html',
        {'ordens': ordens},
    )


def ordem_servico_criar(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)

        if form.is_valid():
            ordem = form.save()
            messages.success(
                request,
                'Ordem de serviço cadastrada com sucesso!',
            )
            return redirect(
                'assistencia:ordem_servico_detalhes',
                pk=ordem.pk,
            )
    else:
        form = OrdemServicoForm()

    return render(
        request,
        'assistencia/ordens/formulario.html',
        {
            'titulo': 'Cadastrar ordem de serviço',
            'modo': 'criar',
            'form': form,
        },
    )


def ordem_servico_detalhes(request, pk):
    ordem = get_object_or_404(
        OrdemServico.objects.select_related(
            'equipamento',
            'equipamento__cliente',
            'tecnico',
        ),
        pk=pk,
    )

    return render(
        request,
        'assistencia/ordens/detalhes.html',
        {'ordem': ordem},
    )


def ordem_servico_editar(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)

    if request.method == 'POST':
        form = OrdemServicoForm(
            request.POST,
            instance=ordem,
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Ordem de serviço atualizada com sucesso!',
            )
            return redirect(
                'assistencia:ordem_servico_detalhes',
                pk=ordem.pk,
            )
    else:
        form = OrdemServicoForm(instance=ordem)

    return render(
        request,
        'assistencia/ordens/formulario.html',
        {
            'titulo': 'Editar ordem de serviço',
            'modo': 'editar',
            'ordem': ordem,
            'form': form,
        },
    )


# =========================
# PAGAMENTOS
# =========================

def pagamentos_lista(request):
    pagamentos = Pagamento.objects.select_related(
        'ordem_servico',
    ).all().order_by('-pk')

    return render(
        request,
        'assistencia/pagamentos/lista.html',
        {'pagamentos': pagamentos},
    )


def pagamento_criar(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)

        if form.is_valid():
            pagamento = form.save()
            messages.success(
                request,
                'Pagamento cadastrado com sucesso!',
            )
            return redirect(
                'assistencia:pagamento_detalhes',
                pk=pagamento.pk,
            )
    else:
        form = PagamentoForm()

    return render(
        request,
        'assistencia/pagamentos/formulario.html',
        {
            'titulo': 'Cadastrar pagamento',
            'modo': 'criar',
            'form': form,
        },
    )


def pagamento_detalhes(request, pk):
    pagamento = get_object_or_404(
        Pagamento.objects.select_related('ordem_servico'),
        pk=pk,
    )

    return render(
        request,
        'assistencia/pagamentos/detalhes.html',
        {'pagamento': pagamento},
    )


def pagamento_editar(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)

    if request.method == 'POST':
        form = PagamentoForm(
            request.POST,
            instance=pagamento,
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Pagamento atualizado com sucesso!',
            )
            return redirect(
                'assistencia:pagamento_detalhes',
                pk=pagamento.pk,
            )
    else:
        form = PagamentoForm(instance=pagamento)

    return render(
        request,
        'assistencia/pagamentos/formulario.html',
        {
            'titulo': 'Editar pagamento',
            'modo': 'editar',
            'pagamento': pagamento,
            'form': form,
        },
    )
